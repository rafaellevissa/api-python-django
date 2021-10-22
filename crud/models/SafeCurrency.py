from django.contrib.auth.models import User
from crud.models.Currency import Currency
from django.db import models
import uuid

class SafeCurrency(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  currency_id = models.ForeignKey(Currency, related_name='crud_safecurrency', on_delete=models.CASCADE, default="")
  user_id = models.ForeignKey(User, related_name='crud_safecurrency', on_delete=models.CASCADE, default="")
  ammount = models.FloatField(default=0)
