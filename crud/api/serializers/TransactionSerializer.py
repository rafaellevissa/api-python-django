from django.db.models import fields
from rest_framework import serializers
from crud.models.Transaction import Transaction

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'