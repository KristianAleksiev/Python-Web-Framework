from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from class_based_views_project.web.models import Todo


# Create your views here.
def index(request):
    context = {
        "title": "Function based view",
    }
    return render(request, "index.html", context)


class IndexView(views.View):
    def get(self, request):
        context = {
            "title": "Class based view",
        }
        return render(request, "index.html", context)


class PetView(views.View):
    http_method_names = ["get", "post"]

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

    def head(self, request):
        pass

    def options(self, request, *args, **kwargs):
        pass

    def trace(self, request):
        pass


class IndexTemplateView(views.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Class based with TemplateView"
        return context
        # return {
        #     "title": "Class based with TemplateView",
        # }


# class PetDetails(views.DetailView):
#     model = Pet  # Model
#     template_name = "pet-details.html"

class RedirectToIndexView(views.RedirectView):
    url = reverse_lazy("index class-based")


class TodoListView(views.ListView):
    model = Todo
    template_name = "todos-list.html"
    ordering = ("title", "category_name")

    context_object_name = "todos"  # Renaming the object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = "todos-details.html"


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = "todo-create.html"
    success_url = reverse_lazy("todos list")
    fields = ("title", "description", "category",)
