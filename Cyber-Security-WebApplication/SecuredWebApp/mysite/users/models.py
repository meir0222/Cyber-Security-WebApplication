from django.db import models
from django.contrib.auth.models import User

# from django.conf import settings


# Create your models here.
class Customer(models.Model):
    cust_id = models.IntegerField()
    cust_name = models.CharField(max_length = 1000)
    cust_email = models.EmailField()
    cust_contact = models.CharField(max_length=1000)

    def __str__(self):
        return self.cust_name


# class UserPasswordHistory(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     password_1 = models.CharField(blank=True, null=True, max_length=128)
#     password_2 = models.CharField(blank=True, null=True, max_length=128)
#     password_3 = models.CharField(blank=True, null=True, max_length=128)
#     password_4 = models.CharField(blank=True, null=True, max_length=128)
#     password_5 = models.CharField(blank=True, null=True, max_length=128)
#     password_6 = models.CharField(blank=True, null=True, max_length=128)
#     password_7 = models.CharField(blank=True, null=True, max_length=128)
#     password_8 = models.CharField(blank=True, null=True, max_length=128)
#     password_9 = models.CharField(blank=True, null=True, max_length=128)
#     password_10 = models.CharField(blank=True, null=True, max_length=128)
#     password_11 = models.CharField(blank=True, null=True, max_length=128)
#     password_12 = models.CharField(blank=True, null=True, max_length=128)
#     password_13 = models.CharField(blank=True, null=True, max_length=128)
#     password_14 = models.CharField(blank=True, null=True, max_length=128)
#     password_15 = models.CharField(blank=True, null=True, max_length=128)
#     password_16 = models.CharField(blank=True, null=True, max_length=128)
#     password_17 = models.CharField(blank=True, null=True, max_length=128)
#     password_18 = models.CharField(blank=True, null=True, max_length=128)
#     password_19 = models.CharField(blank=True, null=True, max_length=128)
#     password_20 = models.CharField(blank=True, null=True, max_length=128)
#     password_21 = models.CharField(blank=True, null=True, max_length=128)
#     password_22 = models.CharField(blank=True, null=True, max_length=128)
#     password_23 = models.CharField(blank=True, null=True, max_length=128)
#     password_24 = models.CharField(blank=True, null=True, max_length=128)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.username + '_password_history'