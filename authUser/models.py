from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # choice = (('DELETED', 'DELETED'),
    #           ('DISABLED', 'DISABLED'),
    #           ('INACTIVE', 'INACTIVE'),
    #           ('DEFAULT', 'DEFAULT'),
    #           ('ACTIVE', 'ACTIVE'),
    #           )
    # types = (('admin', 'admin'), ('normal', 'normal'))
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # last_password_change = models.DateTimeField(null=True)
    # type = models.CharField(max_length=10, choices=types)
    # status = models.CharField(max_length=200, choices=choice, default="DEFAULT")

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


