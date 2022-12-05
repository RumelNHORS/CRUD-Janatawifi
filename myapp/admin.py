from django.contrib import admin
from . models import User, JsonModel

@admin.register(User)
class UserAdminClass(admin.ModelAdmin):
    list_display = ['id', 'date', 'trade_code', 'volume',]

@admin.register(JsonModel)
class Json_Model(admin.ModelAdmin):
    list_display = ['date', 'trade_code', 'volume',]