"""
Database Models.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """For creating a superuser or an admin user which is going to have the access for django admin panel."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


def user_image_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    filename = 'profile_pic.jpeg'
    return f'profile/{instance.user.email}/{filename}'


def user_aadhar_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    return f'profile/{instance.user.email}/{filename}'


def user_pan_upload_path(instance, filename):
    # Assuming the user's name is stored in a field called 'name'
    return f'profile/{instance.user.email}/{filename}'


import os


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Details(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=252)
    aadhar_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to=user_image_upload_path, null=True, blank=True, storage=OverwriteStorage)
    aadhar_file = models.FileField(upload_to=user_aadhar_upload_path, null=True, blank=True, storage=OverwriteStorage)
    pan_file = models.FileField(upload_to=user_pan_upload_path, null=True, blank=True, storage=OverwriteStorage)
    blood_group = models.CharField(max_length=5)

    def __str__(self):
        return f'User: {self.user.name}'
