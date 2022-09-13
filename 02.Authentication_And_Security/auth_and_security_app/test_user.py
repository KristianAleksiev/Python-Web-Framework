from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.http import request

UserModel = get_user_model()
# user_one = UserModel(username="Random1")
# user_one.set_password("abrakadabrapass")
# print(user_one.password)
# user_one.check_password()


# user = UserModel.objects.create_user(username="kris123", password="abrakadabrapass1")
user2 = UserModel.objects.create_user(username="pesho1234", password="abrakadabrapass12")
user3 = UserModel.objects.create_user(username="gosho12345", password="abrakadabrapass123")
user4 = UserModel.objects.create_user(username="test1", password="abrakadabrapass1234")

"""
if request.user.is_authenticated():
    Show/Do something
else:
    Show something else
    
    
Logging a user through a View:
login(request, authenticate(username="x", password="y"))

"""
user5 = authenticate(request, username="username", password="123456")

if user5:
    login(request, user5)