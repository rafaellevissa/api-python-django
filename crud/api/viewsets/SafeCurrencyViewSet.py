from rest_framework.response import Response
from rest_framework import viewsets
from crud.api.serializers.SafeCurrencySerializer import SafeCurrencySerializer
from crud.models.SafeCurrency import SafeCurrency

class SafeCurrencyViewSet(viewsets.ModelViewSet):
  """
    retrieve:
        Return the given safecurrency.

    list:
        Return a list of all safecurrencies.

    create:
        Create a new safecurrency.

    destroy:
        Delete a safecurrency.

    update:
        Update a safecurrency.

    partial_update:
        Update a safecurrency.
  """
  serializer_class = SafeCurrencySerializer
  queryset = SafeCurrency.objects.all()