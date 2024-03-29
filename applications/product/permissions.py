from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.mehtod == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        print(SAFE_METHODS)
        print(request.user)
        print(request.user.is_authenticated)
        print(request.user.is_staff)
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff



class IsAutor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user == obj.owner)