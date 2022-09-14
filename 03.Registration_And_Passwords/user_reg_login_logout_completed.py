from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.views import generic as views

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "first_name", "last_name")


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = "auth/register.html"
    success_url = "/login"

    #  Automated login after registration --->

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = "auth/login.html"


class UserLogoutView(auth_views.LogoutView):
    pass


# Built-in User operations URLS w/o registration ->
path("accounts/", include("django.contrib.auth.urls")),
