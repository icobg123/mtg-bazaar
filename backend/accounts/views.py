import django_filters
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
from .serializers import CardSerializer, MtgShopSerializer

CustomUser = get_user_model()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# class CardListView(generics.ListAPIView):
#     queryset = Cards.objects.all()
#     serializer_class = CardSerializer
#     filter_backends = [filters.SearchFilter]
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     search_fields = ['name']

class CardListView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class MtgShopListView(generics.ListAPIView):
    queryset = MtgShop.objects.all()
    serializer_class = MtgShopSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']
# TODO: Get a list of users when searching by name?
# TODO: Get a list of users when searching by card name
