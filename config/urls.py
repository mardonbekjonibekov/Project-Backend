from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):
    def get(self, request):
        return Response(
            {
                "events": request.build_absolute_uri("/api/events/"),
                "gift_certificates": request.build_absolute_uri("/api/gift-certificates/"),
                "monthly_giving": request.build_absolute_uri("/api/monthly-giving/"),
                "donate_now": request.build_absolute_uri("/api/donate-now/"),
                "cart": request.build_absolute_uri("/api/cart/"),
            }
        )


urlpatterns = [
    path("", lambda request: redirect("api-root"), name="home"),
    path("accounts/profile/", lambda request: redirect("/admin/"), name="profile-redirect"),
    path("admin/", admin.site.urls),
    path("api/", APIRootView.as_view(), name="api-root"),
    path("api/events/", include("events.urls")),
    path("api/gift-certificates/", include("gift_certificates.urls")),
    path("api/monthly-giving/", include("monthly_giving.urls")),
    path("api/donate-now/", include("donations.urls")),
    path("api/cart/", include("cart.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
