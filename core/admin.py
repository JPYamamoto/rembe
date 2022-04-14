from django.contrib import admin
from core.models import Tarjeta
from reversion.admin import VersionAdmin

# Register your models here.

# admin.site.register(Tarjeta)

@admin.register(Tarjeta)
class ModelAdmin(VersionAdmin):
    pass
