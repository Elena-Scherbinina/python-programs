from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #The authenticated user has to be the owner of obj
        #Only owner can delete a card
        return request.user == obj.owner