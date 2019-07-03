from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, default="My Product")
    description = models.TextField(default="Empty Description")
    price = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = serializers.ChoiceField(choices=('AVAILABLE', 'PURCHASED', 'SOLD'))

    def __str__(self):
        return self.name
