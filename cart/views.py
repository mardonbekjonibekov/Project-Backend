from decimal import Decimal

from rest_framework import generics, status
from rest_framework.response import Response

from .models import CartItem
from .serializers import CartItemSerializer


class CartListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        session_key = self.request.session.session_key
        if not session_key:
            return CartItem.objects.none()
        return CartItem.objects.select_related("event").filter(session_key=session_key)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total = sum((item.line_total for item in queryset), Decimal("0.00"))
        count = sum(item.quantity for item in queryset)
        return Response({"items": serializer.data, "count": count, "total": total})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.list(request, *args, **kwargs)


class CartItemDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        session_key = self.request.session.session_key
        if not session_key:
            return CartItem.objects.none()
        return CartItem.objects.filter(session_key=session_key)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        response.status_code = status.HTTP_204_NO_CONTENT
        return response


class CartClearAPIView(generics.GenericAPIView):
    serializer_class = CartItemSerializer

    def delete(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key:
            CartItem.objects.filter(session_key=session_key).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
