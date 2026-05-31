from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GiftCertificateViewSet

router = DefaultRouter()
router.register(r'', GiftCertificateViewSet, basename='giftcertificate')

urlpatterns = [
    path('', include(router.urls)),
]