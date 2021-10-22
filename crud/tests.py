from django.test import TestCase, Client
from django.db import connection, connections, transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from crud.models.Currency import Currency
from crud.models.SafeCurrency import SafeCurrency
from datetime import datetime

factory = Client()

class TransactionTests(TestCase):
    def setUp(self):
        user_password = "teste123"
        self.default_value_in_account = 1000

        self.user_source = User.objects.create(
            password=user_password,
            is_superuser=True,
            username="user1",
            first_name="user1",
            last_name="lastname",
            email="user1@email.com",
            is_staff=False,
            is_active=True,
            date_joined=datetime.now(tz=timezone.utc)
        )

        self.user_received = User.objects.create(
            password=user_password,
            is_superuser=False,
            username="username2",
            first_name="user2",
            last_name="lastname",
            email="user2@email.com",
            is_staff=False,
            is_active=True,
            date_joined=datetime.now(tz=timezone.utc)
        )
        
        self.currency = Currency.objects.create(
            name="Real",
            initials="R$"
        )

        self.safecurrency_source = SafeCurrency.objects.create(
            currency_id=self.currency,
            user_id=self.user_source,
            ammount=self.default_value_in_account
        )

        self.safecurrency_received = SafeCurrency.objects.create(
            currency_id=self.currency,
            user_id=self.user_received,
            ammount=self.default_value_in_account
        )

    def test_should_create_a_trasaction(self):
        requestData = {
            "safe_currency_source_id": self.safecurrency_source.id,
            "safe_currency_received_id": self.safecurrency_received.id,
            "value": self.default_value_in_account - 1
        }

        response = factory.post('/transaction/', requestData)
        safecurrency_source = SafeCurrency.objects.get(id=self.safecurrency_source.id)
        safecurrency_received = SafeCurrency.objects.get(id=self.safecurrency_received.id)

        assert response.status_code == status.HTTP_201_CREATED
        assert safecurrency_source.ammount == self.default_value_in_account - requestData['value']
        assert safecurrency_received.ammount == self.default_value_in_account + requestData['value']

    def test_should_raise_insufficient_fund(self):
        requestData = {
            "safe_currency_source_id": self.safecurrency_source.id,
            "safe_currency_received_id": self.safecurrency_received.id,
            "value": self.default_value_in_account + 1
        }

        response = factory.post('/transaction/', requestData)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_should_raise_object_not_found(self):
        requestData = {
            "safe_currency_source_id": "ec6039bc-eef8-4af4-94c3-616d4db27077",
            "safe_currency_received_id": "c17785e4-edf4-412a-ad92-1afbd618f8a9",
            "value": self.default_value_in_account + 1
        }

        response = factory.post('/transaction/', requestData)

        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_should_raise_validation_error_when_invalid_id_type(self):
        requestData = {
            "safe_currency_source_id": 1,
            "safe_currency_received_id": 2,
            "value": self.default_value_in_account + 1
        }

        response = factory.post('/transaction/', requestData)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
