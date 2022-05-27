from django.contrib import admin
from core.models.tarjeta import Tarjeta
from reversion.admin import VersionAdmin

# Register your models here.

# admin.site.register(Tarjeta)

@admin.register(Tarjeta)
class ModelAdmin(VersionAdmin):
    pass
