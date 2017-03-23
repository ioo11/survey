from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    User,
)
class CustomUser(models.Model):
    """CustomUser"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField(null=True)
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=1, null=True)
    country = models.CharField(max_length=30, null=True)
    sity = models.CharField(max_length=30, null=True)
    reg_date = models.DateField(default=timezone.now())

    @receiver(post_save, sender=User)
    def create_custom_user(instance, created, **kwargs):
        if created:
            print(instance)
            CustomUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_custom_user(sender, instance, **kwargs):
        instance.customuser.save()