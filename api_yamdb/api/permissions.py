from rest_framework import permissions


class IsAdminOrModeratorOrOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
                request.user == obj.author
                or request.user.is_admin
                or request.user.is_moderator
        )
