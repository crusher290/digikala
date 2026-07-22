from django.contrib import admin
from .models import *

@admin.register(CustomerProfile)
class CustomerProfile(admin.ModelAdmin):
    list_display = ("user", "phone", "balance",)
    list_filter = ("user",)


@admin.register(SellerProfile)
class SellerProfile(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("user",)