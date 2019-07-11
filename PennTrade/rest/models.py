from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
    STATUS_CHOICES = ('AVAILABLE', 'PURCHASED', 'SOLD')

    name = models.CharField(max_length=100, blank=False, default="My Product")
    description = models.TextField(default="Empty Description")
    price = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

class Message(models.Model):
    message_subject = models.CharField(max_length=100, blank=True, default="New Message")
    message_body = models.TextField(default="Insert message Here")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever", default=None)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", default=None)
    def __str__(self):
        return self.message_subject