from django.urls import path

from .views import DonationOptionListAPIView

app_name = "donations"

urlpatterns = [
    path("", DonationOptionListAPIView.as_view(), name="donation-option-list"),
]
