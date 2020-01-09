from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.mixins import PermissionMixin
from django.db import models 

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # creates new user

        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionMixin):
    # custom user model thats supports email instead of username
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
