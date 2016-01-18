from django.contrib import admin
from stocklist.models import StockList

# Register your models here.

class StockListAdmin(admin.ModelAdmin):
    pass

admin.site.register(StockList, StockListAdmin)