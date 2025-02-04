from django.shortcuts import render
from rest_framework import generics, permissions
from cards.models import Card, Task
from cards.serializers import CardSerializer, TaskSerializer
from cards.custom_permissions import IsOwnerPermission
from rest_framework.exceptions import PermissionDenied

#Create POST /books
#List    GET /books

# Create your views here.

class CardCollection(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    name = 'card-collection'

    #permission_classes = [
    #    permissions.IsAuthenticated,
    #]
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


    # instead of querying all the customers,
    # I need to filter the customers using the owner field
    def get_queryset(self):
        auth_user = self.request.user
        #current_user = self.request.user
        return Card.objects.filter(owner=auth_user)

    # set owner as the authenticated user
    def perform_create(self, serializer):
        auth_user = self.request.user
        serializer.save(owner=auth_user)


#Retrieve GET /Cards/123
# Update PUT /cards/123
# Destroy  DELETE /cards/123
class CardRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        # the authenticated user has to be the owner of the Card record
        # to be retrieved/updated/destroyed
        #IsOwnerPermission
        IsOwnerPermission
    ]


class TaskCollection(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        # Get the authenticated user
        auth_user = self.request.user
        # Filter tasks by cards owned by the authenticated user
        return Task.objects.filter(card__owner=auth_user)

    #added
    def perform_create(self, serializer):
        auth_user = self.request.user
        card = serializer.validated_data.get('card')  # Get the card from the request
        if card.owner != auth_user:
            raise PermissionDenied("You do not have permission to add tasks to this card.")
        serializer.save()




#Retrieve GET /Cards/123
# Destroy  DELETE /cards/123
#class TaskRecord(generics.RetrieveAPIView):
class TaskRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    #user mary can delete her task
    def perform_destroy(self, instance):
        # Check if the authenticated user owns the associated card
        auth_user = self.request.user
        if instance.card.owner != auth_user:
            raise PermissionDenied("There is no permission to delete this task.")
        instance.delete()

