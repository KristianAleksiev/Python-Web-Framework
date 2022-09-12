from django.contrib import admin

from class_based_views_project.web.models import Todo, Category


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
