"""
1. Caching
- Saving a result of a calculation so the same calculation need not be repeated
- When a cache client attempts to access data, it first checks the cache, and if it's there it returns it
- Otherwise it generates the page and saves it in the cache
- If a change is detected the cache is deleted and the calculation is executed with the new data
- Django has caching (caching the output of specific views, caching the entire site)
- Cache preference -> CACHES

- Redis for caching (instance), settings from docs, redisinsight for visualisation
- pip install redis
- Caching a view -> @cache_page(5) -> django.views.decorators -> Cached for 5 seconds, timeout
- Caching a part of the view -> django.core.cache - Set / Get

2. Session
- A way of server identification of the client
- sessionid
- django_session table
- recognises the user
- different for every client

- Unique session id -> key:value pairs for each session

Cookies data, sent from server->
- Name
- Value
- Domain
- Metadata
- Lifetime (max-age)

3. Middleware
- Executes code-blocks before and after the view is executed
- In settings.py MIDDLEWARE the order matters

def measure_time_middleware(get_response):
    def middleware(request):
        start_time = time.time() -> Code before the view
        response = get_response(request) -> Django pipeline
        end_time = time.time() -> Code after the view

        print(f"Executed in {end_time - start_time}s)
    return response

4. Signals
- Executed on pre-defined events
- Before / after creation, before / after deletion (models)
- When a user is registered f.e. send an email

from django.dispatch import receiver
from django.db.models.signals import pre_save

@receiver(pre_save, sender=Profile) post_save, pre_delete, post_delete
def profile_created(**kwargs):
    pass

5. Pagination
- The returned data is displayed on multiple pages within one web page

profiles = Profile.objects.all()
paginator = Paginator(profiles, per_page=5)
current_page = request.GET.get("page", 1)
context => "profiles_page": paginator.get_page(current_page)


class ProfileListView(ListView):
    model = Profile
    template_name = "profile.html"
    paginate_by = 5

    def get_paginate_by(self, queryset):
        pass
"""
