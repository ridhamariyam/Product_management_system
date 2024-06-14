from django.http import HttpResponseForbidden

class IsAdminUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Admin').exists():
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class IsStoreKeeperUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Storekeeper').exists():
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class IsCustomerUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Customer').exists():
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)