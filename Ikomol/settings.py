from pathlib import Path

# from decouple import config
import os
from dotenv import load_dotenv
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = os.getenv("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    # created apps
    "core",
    "blog",
    "Career",
    # installed apps
    "django_extensions",
    "storages",
    "ckeditor",
    "django_browser_reload",
    "defender",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "crispy_forms",
    "crispy_bootstrap5",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "Ikomol.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "blog_tags": "blog.templatetags.blog_tags",
                "recent_blogs": "blog.templatetags.recent_blogs",
            },
        },
    },
]
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

SITE_ID = 1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
LOGIN_REDIRECT_URL = "/admin"
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": os.getenv("client_id"),
            "secret": os.getenv("secret"),
            "key": "",
        }
    }
}

WSGI_APPLICATION = "Ikomol.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1200),
}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "NAME": os.getenv("NAME"),
        "NAME": "Ikomol",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        # "HOST":"tech_db",
        # "PORT": os.getenv("PORT"),
        "PORT": "5432",
        #
    }
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
RECIPIENT_ADDRESS = os.getenv("RECIPIENT_ADDRESS")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

USE_S3 = os.getenv('USE_S3') == 'TRUE'
if USE_S3:

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_QUERYSTRING_AUTH = False
AWS_S3_OBJECT_PARAMETERS = {"Access-Control-Allow-Origin": "*"}
# s3 static settings
AWS_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATIC_URL = "/static/"
# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR / "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR / "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CKEDITOR_UPLOAD_PATH = "blogs/blog_images/"
MEDIA_ROOT = os.path.join(BASE_DIR / "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# security settings
# after https is configured
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# # content security policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)

# # http sttrict transport security
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# # SECURE SSL REDIRECT
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "djangoapp.log",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Ikomol-Internet Admin",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Ikomol-Internet",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Ikomol-Internet",
    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "images/Ikomol-Internet1.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Ikomol-Internet",
    # Copyright on the footer
    "copyright": "Ikomol-Internet Ltd",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    # "search_model": ["auth.User", "job.Job"],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        {"name": "Homepage", "url": "home", "new_window": True},  #
        # model admin to link to (Permissions checked against model)
        {"app": "Career"},
        {"model": "blog.Blog"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"model": "core.Service"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"},
        # {'app':'Account'}
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": [
    #     "auth",
    #     "Job",
    #     "Blog",
    # ],
    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "blog": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fa-regular fa-blog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "blog.Blog": "fas fa-blog",
        "blog.Comment": "fas fa-comments",
        # "accounts.Profile":"fas fa-id-card",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    # "language_chooser": True,
}
# JAZZMIN_UI_TWEAKS = {
    # "theme": "flatly",
    # "dark_mode_theme": "cyborg",
# }

sentry_sdk.init(
    dsn="https://e23e5d2d7ba74c1dbf91947d1bcb6370@o4504099387342848.ingest.sentry.io/4504099601973248",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
