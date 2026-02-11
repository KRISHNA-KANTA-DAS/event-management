from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    membership = models.ForeignKey(
        'Membership',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Membership(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name
