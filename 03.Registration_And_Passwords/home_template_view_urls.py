from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("registration_password_app.demo.urls")),
    #  Without context, straightforward
    path("", TemplateView.as_view(template_name="index.html"), name="index")
]