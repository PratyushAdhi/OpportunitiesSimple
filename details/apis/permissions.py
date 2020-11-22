from rest_framework import permissions

class IsAuthorOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif request.user == obj.user:
            return True
        return False
        