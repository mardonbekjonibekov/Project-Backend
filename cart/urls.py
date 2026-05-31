from django.urls import path

from .views import CartClearAPIView, CartItemDestroyAPIView, CartListCreateAPIView

app_name = "cart"

urlpatterns = [
    path("", CartListCreateAPIView.as_view(), name="cart-list-create"),
    path("clear/", CartClearAPIView.as_view(), name="cart-clear"),
    path("<int:pk>/", CartItemDestroyAPIView.as_view(), name="cart-item-delete"),
]
