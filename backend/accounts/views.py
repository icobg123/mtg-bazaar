from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, authentication

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

from . import serializers
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from .serializers import CardSerializer

CustomUser = get_user_model()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Cards.objects.all()


# class CardListView(generics.ListAPIView):
#     queryset = Cards.objects.all()
#     serializer_class = CardSerializer
#     filter_backends = [filters.SearchFilter]
#     # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     search_fields = ['name']

class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
