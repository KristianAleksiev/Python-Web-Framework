from django.http import HttpResponse


def allowed_groups(roles=None):
    if roles is None:
        roles = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Not allowed to view")

        return wrapper

    return decorator


def permissions(permissions_required):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated and not user.has_perms(permissions_required):
                return HttpResponse("No permission")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
