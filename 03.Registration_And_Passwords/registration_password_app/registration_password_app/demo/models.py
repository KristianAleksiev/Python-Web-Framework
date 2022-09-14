from django.contrib.auth import models as auth_models
from django.db import models
from registration_password_app.demo.managers import AppUsersManager


# Create your models here.
# UserModel = get_user_model()
#
#
# class Profile(models.Model):
#     # fields
#     # img
#     # date_of_birth
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


# Completely custom user model
# class AppUser:
#     pass
#     # email
#     # pass
#     # is_staff
#     # is_superuser
#
#
# class Profile:
#     # first name
#     # last name
#     # profile img
#     user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

# N.B.! CREATE BEFORE INITIAL MIGRATIONS !!! # N.B.! CREATE BEFORE INITIAL MIGRATIONS !!!
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False, )  # 1
    date_joined = models.DateTimeField(auto_now_add=True, )
    is_superuser = models.BooleanField(default=False, )
    is_staff = models.BooleanField(default=False, )
    USERNAME_FIELD = "email"

    objects = AppUsersManager()  # 3


class Profile(models.Model):
    first_name = models.CharField(max_length=25, )
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)


"""
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model (SETTINGS) AUTH_USER_MODEL = "app_name.AppUser"
3. Create a manager for users
"""
