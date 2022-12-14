from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class ObjectPermission(permissions.BasePermission):
    message = 'Permission Denied, unauthorised'
    methods = ('PUT', 'DELETE', 'GET')

    # def has_permisatsion(self, request, view):
    #     retur
    # n True

    def has_object_permission(self, request, view, obj):
        print(request.method in self.methods, obj.id, request.user.id)
        if obj.author.id != request.user.id:
            raise PermissionDenied(self.message)
        return True
