from django.contrib import admin
from .models import NewCustomer

# Register your models here.

class adminYazı(admin.ModelAdmin):
    list_display = ["name", "surname", "date"]
    list_filter = ["date"]
    search_fields = ["name", "surname"]
    class Meta:
        model = NewCustomer

admin.site.register(NewCustomer,adminYazı)