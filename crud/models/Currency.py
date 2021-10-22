from django.db import models
import uuid

class Currency(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255)
  initials = models.CharField(max_length=10)

  def __str__(self):
    return self.name