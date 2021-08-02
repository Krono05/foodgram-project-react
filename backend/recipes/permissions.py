from rest_framework.permissions import SAFE_METHODS, BasePermission

CHANGE_METHODS = ['PUT', 'PATCH', 'DELETE']


class AdminOrAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated if request.method == 'POST'
            else True
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user == obj.author
            or user.is_superuser
            or user.is_admin()
            if request.method in CHANGE_METHODS and not user.is_anonymous
            else
            request.method in SAFE_METHODS
        )
