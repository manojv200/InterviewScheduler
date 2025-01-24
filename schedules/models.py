
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class TblUsers(AbstractUser):
    user_type_id = models.CharField(null=True, blank=True, max_length=255)
    user_type = models.CharField(null=True, blank=True, max_length=255)
    start_date = models.IntegerField(null=True, blank=True)
    end_date = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'