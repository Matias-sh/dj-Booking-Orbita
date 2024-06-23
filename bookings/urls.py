from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, SpaceViewSet, ServiceViewSet, BookingViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'spaces', SpaceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
