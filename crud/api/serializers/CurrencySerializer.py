from django.db.models import fields
from rest_framework import serializers
from crud.models.Currency import Currency

class CurrencySerializer(serializers.ModelSerializer):
  class Meta:
    model = Currency
    fields = '__all__'