import os
from pathlib import Path
 
import dj_database_url
from django.urls import reverse_lazy
 
BASE_DIR = Path(__file__).resolve().parent.parent
 
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,0.0.0.0").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000,http://localhost:8000,http://127.0.0.1:8000",
).split(",")
 
INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "events",
    "gift_certificates",
    "monthly_giving",
    "donations",
    "cart",
]
 
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",        # ← ENG BIRINCHI bo'lishi SHART
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
 
ROOT_URLCONF = "config.urls"
 
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
 
WSGI_APPLICATION = "config.wsgi.application"
 
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}
 
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
 
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
 
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
 
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "/admin/"
LOGOUT_REDIRECT_URL = "/admin/login/"
 
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}
 
# CORS — barcha originlarga ruxsat
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
 
UNFOLD = {
    "SITE_TITLE": "Lookingglass Owner Admin",
    "SITE_HEADER": "Lookingglass Theatre",
    "SITE_SUBHEADER": "Events, donations, certificates and cart content",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": "confirmation_number",
        "dark": "confirmation_number",
    },
    "COLORS": {
        "primary": {
            "50": "255 247 237",
            "100": "255 237 213",
            "200": "254 215 170",
            "300": "253 186 116",
            "400": "251 146 60",
            "500": "249 115 22",
            "600": "234 88 12",
            "700": "194 65 12",
            "800": "154 52 18",
            "900": "124 45 18",
            "950": "67 20 7",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Storefront",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Events",
                        "icon": "event",
                        "link": reverse_lazy("admin:events_event_changelist"),
                    },
                    {
                        "title": "Gift Certificates",
                        "icon": "redeem",
                        "link": reverse_lazy("admin:gift_certificates_giftcertificateorder_changelist"),
                    },
                    {
                        "title": "Monthly Giving",
                        "icon": "favorite",
                        "link": reverse_lazy("admin:monthly_giving_monthlygivingoption_changelist"),
                    },
                    {
                        "title": "Donate Now",
                        "icon": "volunteer_activism",
                        "link": reverse_lazy("admin:donations_donationoption_changelist"),
                    },
                    {
                        "title": "Cart Items",
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:cart_cartitem_changelist"),
                    },
                ],
            },
            {
                "title": "Access",
                "separator": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Groups",
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
 
# Cross-site session cookie settings
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
 