import django_filters.rest_framework

from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import filters


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


