from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from .serializers import CardSerializer, MtgShopSerializer, WantsSerializer, \
    TradesSerializer
from .models import *
import django_filters
from . import serializers

CustomUser = get_user_model()


class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'%s__%s' % (self.field_name, self.lookup_expr): integers})
        return qs


class CardIdsFilter(django_filters.FilterSet):
    ids = ListFilter(field_name="id", lookup_expr='in')

    class Meta:
        model = Cards
        fields = ['ids']


class CardsIdsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_backends = (DjangoFilterBackend,)
    filter_class = CardIdsFilter


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Cards.objects.all()


class TradesViewSet(viewsets.ModelViewSet):
    serializer_class = TradesSerializer
    # serializer_class = TradesSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Trades.objects.all()


class WantsViewSet(viewsets.ModelViewSet):
    serializer_class = WantsSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Wants.objects.all()


class MtgShopViewSet(viewsets.ModelViewSet):
    serializer_class = MtgShopSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = MtgShop.objects.all()
