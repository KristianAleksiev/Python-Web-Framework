"""
1. What are class based views?
- Alternative way to implement views as Python objects in stead of functions
- An object from class is called like a function (override the __call__ dunder)
- Automated context building -> If POSt, If GET

from django.views import generic as views
class PetView(views.View): <--
    def get(self, request):
        pass

    def post(self, request):
        pass

- In stead of checking the request method => going into the class method
- Higher abstraction on function based views
- Easily extended, harder to implement (not straightforward)
- Extensive use of mixins, harder to read than FBV
- Handling HTTP methods in separate class methods
- Built-in generic CBVs:

--------------------------------------------------------------

2. Base Views
- Parent views, could be used by themselves or inherited from
- Provide much of the needed functionality to create Django views
- View class -> views.View -> Handling HTTP methods - master class
    http_method_names = ["get","post","put","patch","delete","head","options","trace",]

    urlpatterns = [path("cbv/", IndexView.as_view(), name="index class-based")] <= Class.as_view() in URLs

DetailView:
class PetDetails(views.DetailView):
    model = Pet # Model
    template_name = "pet-details.html"

TemplateView:
Variant 1 ->
class IndexTemplateView(views.TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        return {
            "title": "Class based with TemplateView",
        }  <- To show something without context

Variant 2 ->
class IndexTemplateView(views.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Class based with TemplateView"
        return context

RedirectView:
Variant 1->
class RedirectToIndexView(views.RedirectView):
    url = reverse_lazy("index class-based")

Variant 2 -> Branching
class RedirectToIndexView(views.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if ...:
            return "place one"
        else:
            return "place two"

--------------------------------------------------------------

3. Generic Views
- Display
- Create, update, delete

- List View

class TodoListView(views.ListView):
    model = Todo
    template_name = "todos-list.html"
    ordering = ("title", "category_name")
    context_object_name = "todos" # Renaming the object_list <--------------

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
{% for todo in object_list %} <---------------

- Detail View - Works with a single object
class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = "todos-details.html"

--------------------------------------------------------------

CRUD Views:

- Create View ->
class TodoCreateView(views.CreateView):
    model = Todo
    template_name = "todo-create.html"
    success_url = reverse_lazy("todos list")
    fields = ("title", "description", "category",)

- Update View ->
class TodoUpdateView(views.UpdateView):
    model = Todo
    template_name = "todo-create.html"
    fields = ("title", "description", "category",)

- Delete View ->
class TodoDeleteView(views.DeleteView):
    model = Todo
    template_name = "todo-delete.html"
    fields = "__all__"
    success_url = reverse_lazy("todos list") - Mandatory




--------------------------------------------------------------
4. Useful CBVs Methods
- dispatch() - Accepts request and renders, request method to view, self.object to self.get_object, access control
- get_object() - Gets a single object
- get_queryset() - (objects.all()) - Managers
- get_context_data() - context["title"] = " Extended with custom content "
- get_template_names() - admin template, regular template


"""