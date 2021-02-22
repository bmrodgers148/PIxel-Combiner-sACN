from django.contrib import admin
from .models import Pixel, Universe, AppSettings

# Register your models here.
admin.site.register(Pixel)
admin.site.register(Universe)
admin.site.register(AppSettings)
