from django.test import TestCase, Client
from django.db import connection, connections, transaction
from rest_framework import status
from django.contrib.auth.models import User
from crud.models.Currency import Currency
from crud.models.SafeCurrency import SafeCurrency
from datetime import datetime


client = Client()

class TransactionTests(TestCase):
    def setUp(self):
        connections.databases['test']['ATOMIC_REQUESTS'] = True

        self.user_source = User.objects.create(
            password="teste123",
            is_superuser=False,
            username="user1",
            first_name="user1",
            last_name="lastname",
            email="user1@email.com",
            is_staff=False,
            is_active=True,
            date_joined=datetime.now()
        )
        self.user_received = User.objects.create(
            password="teste123",
            is_superuser=False,
            username="user2",
            first_name="user2",
            last_name="lastname",
            email="user2@email.com",
            is_staff=False,
            is_active=True,
            date_joined=datetime.now()
        )
        self.currency = Currency.objects.create(
            name="Real",
            initials="R$"
        )
        self.safecurrency_source = SafeCurrency.objects.create(
            currency_id=currency.id,
            user_id=user_source.id,
            ammount=1000
        )
        self.safecurrency_received = SafeCurrency.objects.create(
            currency_id=currency.id,
            user_id=user_received.id,
            ammount=1000
        )

    def tearDown(self):
        connections.databases['test']['ATOMIC_REQUESTS'] = False

    def test_should_create_a_trasaction():
        requestData = {
            "safe_currency_source_id": user_source.id,
            "safe_currency_received_id": user_received.id,
            "value": 500
        }

        response = client.post('/transaction/', requestData)

        print(response.content)

        assert response.status_code == status.HTTP_201_CREATED
        