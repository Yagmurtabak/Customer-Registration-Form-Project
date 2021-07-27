from django.contrib import admin
from .models import NewCustomer

# Register your models here.

class adminYazı(admin.ModelAdmin):
    list_display = ["Name", "Surname", "Date"]
    list_filter = ["Date"]
    search_fields = ["Name", "Surname"]
    class Meta:
        model = NewCustomer

admin.site.register(NewCustomer,adminYazı)