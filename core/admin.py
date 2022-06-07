from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from core.models.tarjeta import Tarjeta
from core.models.token import Token

# Register your models here.

admin.site.register(Tarjeta, SimpleHistoryAdmin)
admin.site.register(Token, SimpleHistoryAdmin)
