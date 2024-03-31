from django.db import models


class Subscriber(models.Model):
    """A model to store subscriber details."""
    email = models.EmailField(max_length=200, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
