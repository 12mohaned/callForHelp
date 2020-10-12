from django.contrib import admin

# Register your models here.
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    fields = ["name", "image"]
admin.site.register(Country, CountryAdmin)
