from django.contrib.auth import login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.views import generic as views

# def my_view(request):
#     user = None
#     login(request, user)


# From beginning...
# class UserRegistrationView(CreateView):
#     model = User


UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)


# Creating register form from built-in
class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm  # ModelForm
    template_name = "auth/register.html"
    success_url = "/login"

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


# Addition register info, switch the form_class in the UserRegistrationView (UserRegistrationForm)


# Login

# def login_user(request):
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     user = UserModel.objects.get(username=username)
#     login(request, user)

class UserLoginView(auth_views.LoginView):
    template_name = "auth/login.html"

# Logout

class UserLogoutView(auth_views.LogoutView):
    pass