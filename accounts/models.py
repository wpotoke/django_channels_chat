from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .manager import MyUserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    username_regex = RegexValidator(
        regex=r"^[A-Za-z_]+$", message="username must be contained only A-Z a-z and _"
    )
    username = models.CharField(
        validators=[username_regex, MinLengthValidator(5)], max_length=15, unique=True, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()

    phone_regex = RegexValidator(
        regex=r"^((\+7)|8)\d{10}$",
        message="Phone number must be entered in the format: '+79999999999' or '89999999999'.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=12, null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
