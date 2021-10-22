from rest_framework.response import Response
from rest_framework import viewsets
from crud.api.serializers.TransactionSerializer import TransactionSerializer
from crud.models.Transaction import Transaction
from crud.models.SafeCurrency import SafeCurrency
from django.forms.models import model_to_dict
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from crud.exceptions import InsufficientFunds
from django.db import transaction

class TransactionViewSet(viewsets.ModelViewSet):
  """
    retrieve:
        Return the given transaction.

    list:
        Return a list of all transactions.

    create:
        Create a new transaction.

    destroy:
        Delete a transaction.

    update:
        Update a transaction.

    partial_update:
        Update a transaction.
  """
  serializer_class = TransactionSerializer
  queryset = Transaction.objects.all()

  @transaction.atomic
  def create(self, request):
    try:
      safe_currency_source_id = request.data["safe_currency_source_id"]
      value = float(request.data["value"])

      safe_currency = SafeCurrency.objects.get(id=safe_currency_source_id)
      safe_currency_dict = model_to_dict(safe_currency)

      if(safe_currency_dict["ammount"] >= value):
        total_ammount = safe_currency_dict["ammount"] - value
        safe_currency.ammount = total_ammount
        safe_currency.save(update_fields=["ammount"])
      else:
        raise InsufficientFunds(safe_currency_dict["ammount"])

      safe_currency_received_id = request.data["safe_currency_received_id"]
      safe_currency_received = SafeCurrency.objects.get(id=safe_currency_received_id)
      safe_currency_received_dict = model_to_dict(safe_currency_received)

      total_ammount = safe_currency_received_dict["ammount"] + value
      safe_currency_received.ammount = total_ammount
      safe_currency_received.save(update_fields=["ammount"])

      obj_store, created = Transaction.objects.update_or_create(
        safe_currency_source_id=safe_currency_source_id,
        safe_currency_received_id=safe_currency_received_id,
        created_at=datetime.now(tz=timezone.utc),
        value=value
      )

      return Response(model_to_dict(obj_store), 201)
    except ObjectDoesNotExist as error:
      return Response({ "error": str(error) }, 404)
    except InsufficientFunds as error:
      return Response({ "error": error.message }, 401)
    except ValidationError as error:
      return Response({ "error": error.message }, 400)
    except Exception as e:
      return Response({ "error": str(e) }, 500)

