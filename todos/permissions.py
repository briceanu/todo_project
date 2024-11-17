from rest_framework.permissions import BasePermission


class IsAuthenticatedAndOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.username)
        print(obj.user.username)
        #  checking to see if the user is authenticated and owns the todo
        return request.user.is_authenticated and request.user.username == obj.user.username
