from django.contrib import admin
from .models import Crop


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'msp', 'stock', 'location')

admin.site.register(Crop)
