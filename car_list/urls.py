from rest_framework.routers import DefaultRouter

from .views import CarListViewSet

router = DefaultRouter()
router.register('car_list', CarListViewSet)

