"""dtc_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from core.views import IndexTemplateView
from dtc_server.settings import MEDIA_ROOT
import os

DIST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dtc_vue/dist')

urlpatterns = [
    path('admin', admin.site.urls),
    # Get builded files by django.views.static
    url(r'^media/(?P<path>.*)$', serve, {"document_root": DIST_DIR}),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
