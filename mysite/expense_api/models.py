from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type