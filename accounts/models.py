from django.db import models
from django.contrib.auth.models import User



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self) -> str:
        return f'{self.user.username} with {self.phone}'


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


