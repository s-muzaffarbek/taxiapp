from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapp.viewsets import DriverAPIView, PassengerAPIView, RoadAPIView, StationAPIView, CarAPIView

router = DefaultRouter()
router.register('driver', DriverAPIView)
router.register('passenger', PassengerAPIView)
router.register('road', RoadAPIView)
router.register('station', StationAPIView)
router.register('car', CarAPIView)


urlpatterns = [
    # path('driver/', DriverAPIView.as_view({'get': 'list'}), name='driver'),
    # path('passenger/', PassengerAPIView.as_view(), name='driver')
    path('', include(router.urls))
]
