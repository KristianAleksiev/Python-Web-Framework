from django.urls import path

from class_based_views_project.web.views import index, IndexView, IndexTemplateView, TodoListView, TodoDetailsView, \
    TodoCreateView

urlpatterns = [
    path("", index, name="index func-based"),
    path("cbv/", IndexView.as_view(), name="index class-based"),
    path("cbv-template/", IndexTemplateView.as_view(), name="index class-based template"),
    path("todos-list/", TodoListView.as_view(), name="todos list"),
    path("todos-details/<int:pk>/", TodoDetailsView.as_view(), name="todos details"),
    path("todos/create/", TodoCreateView.as_view(), name="todo create"),


]
