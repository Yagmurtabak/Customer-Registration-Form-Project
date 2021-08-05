from django.contrib import admin
from .models import Customer

# Register your models here.

class admincustomer(admin.ModelAdmin):
    list_display = ["name", "surname", "date"]
    list_filter = ["date"]
    search_fields = ["name", "surname"]
    class Meta:
        model = Customer

admin.site.register(Customer,admincustomer)