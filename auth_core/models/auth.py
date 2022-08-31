from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from .base import TimeStampModel


class User(AbstractUser, PermissionsMixin, TimeStampModel):

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='stf_user_email_idx'),
            models.Index(fields=['username'], name='stf_user_username_idx'),
        ]
        db_table = "user"
