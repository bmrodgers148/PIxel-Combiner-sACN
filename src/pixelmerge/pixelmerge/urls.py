"""pixelmerge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from configurator.views import (
    home_view, settings_view, pixel_view, delete_pixel_view, universe_view,
    delete_universe_view, refresh_universes, start_sACN_view, stop_sACN_view, 
    export_data, pixel_upload, universe_upload)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('settings/', settings_view, name="settings"),
    path('pixel/<str:pk>/', pixel_view, name="pixel"),
    path('delete_pixel/<str:pk>/', delete_pixel_view, name="delete_pixel"),
    path('universe/<str:pk>/', universe_view, name="universe"),
    path('delete_universe/<str:pk>/', delete_universe_view, name="delete_universe"),
    path('refresh_universes', refresh_universes, name="refresh_universes"),
    path('stop_sacn', stop_sACN_view, name="stop_sacn"),
    path('start_sacn', start_sACN_view, name="start_sacn"),
    path('export/<str:pk>/', export_data, name="export"),
    path('pixel_upload', pixel_upload, name="pixelupload"),
    path('universe_upload', universe_upload, name="uniupload"),
]
