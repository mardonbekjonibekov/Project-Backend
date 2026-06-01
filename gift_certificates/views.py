import os
import stripe
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dotenv import load_dotenv

from .models import GiftCertificateOrder
from .serializers import GiftCertificateOrderSerializer

# .env.local faylini topish (backend papkasidan ikki qadam tepaga chiqadi)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV_PATH = os.path.join(BASE_DIR, '.env.local')
load_dotenv(dotenv_path=ENV_PATH)

# Stripe-ni sozlash
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


class GiftCertificateViewSet(viewsets.ModelViewSet):
    queryset = GiftCertificateOrder.objects.all()
    serializer_class = GiftCertificateOrderSerializer


@api_view(['POST'])
def create_payment_intent(request):
    try:
        data = request.data
        amount = data.get('amount')  # Frontenddan keladigan summa

        if not amount:
            return Response({"error": "Suma kiritilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        # Sentga o'giramiz (20$ -> 2000 sent)
        amount_in_cents = int(float(amount) * 100)

        # Stripe niyatini yaratamiz
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )

        return Response({
            'clientSecret': intent['client_secret']
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)