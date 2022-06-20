from django.db import models
from django.contrib.auth import get_user_model

# Model for User entities
# It's the default provided by Django.
User=get_user_model()

class Token(models.Model):
    """Model for tokens used by the Google Calendar API.
    Fields:
        - token: the current token to be used.
        - refresh_token: the token to be used when the `token` expires.
        - user: the user the token is attached to.
    """

    token = models.CharField(max_length=2100)
    refresh_token = models.CharField(max_length=2100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
