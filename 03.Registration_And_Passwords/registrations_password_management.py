"""
1. Registration
- Built-in form in django - UserCreationForm, connected to the User model
- Comes with three fields (username, pass1, pass2)
- w/o UserCreation ->

class UserRegistrationView(CreateView):
    model = User

- With UserCreation ->

from django.views import generic as views
from django.contrib.auth import forms as auth_forms
class UserRegistrationView(views.CreateView):
    form_class = auth_forms.UserCreationForm  # ModelForm
    template_name = "auth/register.html"

-
class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "first_name", "last_name")

class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm  # ModelForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("index")

- Creating a custom class with desired fields


2. Extending the Django User Model
- Model inheritance without new table
- Own table with One-To-One relationship
UserModel = get_user_model()
class Profile(models.Model):
    #fields
    #img
    #date_of_birth
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
- Extending AbstractBaseUser
- New user model that inherits from AbstractBaseUser

3. Login/Logout
- LoginView, LogoutView built-in
- ?next=
- Settings -> LOGIN_URL, LOGOUT_REDIRECT_URL

4. Password management
- Django provides secure way of managing passwords -> PBKDF2 algo with SHA256 hash
- Passwords go through hashing algorithm

"""