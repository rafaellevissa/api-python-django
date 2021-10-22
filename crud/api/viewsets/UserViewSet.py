from rest_framework.response import Response
from rest_framework import viewsets
from crud.api.serializers.UserSerializer import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
  """
    retrieve:
        Return the given user.

    list:
        Return a list of all users.

    create:
        Create a new user.

    destroy:
        Delete a user.

    update:
        Update a user.

    partial_update:
        Update a user.
  """

  serializer_class = UserSerializer
  queryset = User.objects.all() 