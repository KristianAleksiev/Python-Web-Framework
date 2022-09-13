from django.contrib.auth.models import User

UserModel = get_user_model()
user = UserModel.objects.create_user(username="kris123", password="abrakadabrapass1")

#  Authentication
user = authenticate(request, username="username", password="123456")

#  Authorization
if user:
    login(request, user5)

#  CRUD permissions -> auth_permissions
if user.has_perm("web.change_category"):
    category = Category.objects.get(pk=X)
    category.name = "Another name"
    category.save()

#  Permission control
# > Function based views:
@login_required
def index(request):
    pass
