from django.db import models
import uuid

class Transaction(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  safe_currency_source_id = models.UUIDField(default=uuid.uuid4)
  safe_currency_received_id = models.UUIDField(default=uuid.uuid4)
  value = models.FloatField()
  created_at = models.DateTimeField(auto_created=True)
