from rest_framework.response import Response
from rest_framework import viewsets
from crud.api.serializers.CurrencySerializer import CurrencySerializer
from crud.models.Currency import Currency

class CurrencyViewSet(viewsets.ModelViewSet):
  """
    retrieve:
        Return the given currency.

    list:
        Return a list of all currencies.

    create:
        Create a new currency.

    destroy:
        Delete a currency.

    update:
        Update a currency.

    partial_update:
        Update a currency.
  """
  serializer_class = CurrencySerializer
  print(type(Currency))
  queryset = Currency.objects.all()