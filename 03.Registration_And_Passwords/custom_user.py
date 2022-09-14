"""
STEPS FOR CREATING CUSTOM DATA USERS

1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model (SETTINGS) AUTH_USER_MODEL = "app_name.AppUser" -> get_user_model()
3. Create a manager for users
"""
from django.contrib.auth import models as auth_models
from django.db import models
from registration_password_app.demo.managers import AppUsersManager


# Create your models here.
# N.B.! CREATE BEFORE INITIAL MIGRATIONS !!!

class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False, )  # 1
    date_joined = models.DateTimeField(auto_now_add=True, )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"  # <--------

    objects = AppUsersManager()  # 3


# ADDITIONAL EXTENSION OF THE USER
class Profile(models.Model):
    first_name = models.CharField(max_length=25, )

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

# Register form field view fix ->
UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)
