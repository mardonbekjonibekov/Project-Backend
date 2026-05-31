from django.urls import path

from .views import MonthlyGivingListAPIView

app_name = "monthly_giving"

urlpatterns = [
    path("", MonthlyGivingListAPIView.as_view(), name="monthly-giving-list"),
]
