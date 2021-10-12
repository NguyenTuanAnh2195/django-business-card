from rest_framework import permissions


class IsSelfOrAdminOrReadOnly(permissions.BasePermission):
    """

    Allow each user to only edit their own information
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id or request.user.is_staff
