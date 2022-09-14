from django.views import generic as views
from django.contrib.auth import forms as auth_forms

# class UserRegistrationView(views.CreateView):
#     form_class = auth_forms.UserCreationForm  # ModelForm
#     template_name = "auth/register.html"


#  Custom registration form:
UserModel = get_user_model()


# Form fields = > username, mail, fn, ln, pass1, confirmpass
class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "first_name", "last_name")


# Creating register form from built-in
class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm  # ModelForm
    template_name = "auth/register.html"
    success_url = "/"
