from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GiftCertificateViewSet, create_payment_intent # 👈 funksiyani import qiling

router = DefaultRouter()
router.register(r'gift-certificates', GiftCertificateViewSet)

urlpatterns = [
    # 🔥 MUHIM: Routerning URL-laridan TEPADA turishi kerak!
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
    
    # Qolgan standart yo'nalishlar router orqali ishlaydi
    path('', include(router.urls)),
]