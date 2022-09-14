# Manually:
def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = UserModel.objects.get(username=username)
    login(request, user)


# Django Built-in LoginView:
from django.contrib.auth import views as auth_views


class UserLoginView(auth_views.LoginView):
    template_name = "auth/login.html"

# LOGIN_URL
# LOGOUT_REDIRECT_URL  -> Settings
