"""Ikomol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import stat
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views  # new


urlpatterns = [
    path(
        "admin/login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("admin/", admin.site.urls, name="admin"),
    path("accounts/", include("allauth.urls")),
    path("", include("core.urls")),
    path("", include("blog.urls")),
    path("careers", include("Career.urls")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler500 = "core.views.error_500"
# handler404 = 'core.views.error_404'
admin.site.site_header = "iKomol Internet"
