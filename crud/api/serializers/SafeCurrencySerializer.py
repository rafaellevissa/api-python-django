from django.db.models import fields
from rest_framework import serializers
from crud.models.SafeCurrency import SafeCurrency

class SafeCurrencySerializer(serializers.ModelSerializer):
  class Meta:
    model = SafeCurrency
    fields = '__all__'