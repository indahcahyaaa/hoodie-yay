import uuid
from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.URLField()

    
