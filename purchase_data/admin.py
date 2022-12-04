from django.contrib import admin
from .models import PurchaseData, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(PurchaseData)