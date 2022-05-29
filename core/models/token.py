from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Token(models.Model):
    token = models.CharField(max_length=2100)
    refresh_token = models.CharField(max_length=2100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
