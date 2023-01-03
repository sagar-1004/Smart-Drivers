from django.db import models

import uuid

# # Create your models here.

# # Model for details of plots


class driver(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    address = models.DateField(auto_now=True)
    phone = models.CharField(max_length=10)
