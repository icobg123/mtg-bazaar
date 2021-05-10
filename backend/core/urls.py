from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(r'recipes', RecipeViewSet)
# router.register(r'cards', CardListView)
# router.register(r'cards', CardViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    # path('card-search/', CardListView.as_view()),
    # path('api/cards/', CardListView.as_view(), name="cards"),

]
