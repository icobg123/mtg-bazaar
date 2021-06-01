from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *
from .viewsets import *

from . import routers, views

router = DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'cards-ids', CardsIdsViewSet)
router.register(r'shops', MtgShopViewSet)
router.register(r'wants', WantsViewSet)
router.register(r'trades', TradesViewSet)

urlpatterns = [
    path('accounts/data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),  # get data for the currently logged in user
    path('accounts/users/', include(routers.router.urls)),  # provides a few default
    path('card-search/', CardListView.as_view()),
    path('shop-search/', MtgShopListView.as_view()),
    # path('card-id-search/', CardsIdsViewSet),
    # path('card-id-search/', CardsIdsViewSet.as_view()),
    path("", include(router.urls)),

    # views that we can use for our CRUD operations.
]
