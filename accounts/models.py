from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    Permission,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True,  **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(
                email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )

        if password:
            user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    age = models.IntegerField(blank=True, null=True)
    birth_day = models.DateTimeField(blank=True, null=True)
    job_title = models.CharField(max_length=256, blank=True)
    employer = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)
    profile_picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ("email", )

