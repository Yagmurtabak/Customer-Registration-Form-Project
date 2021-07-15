from django.contrib import admin
from .models import yazı

# Register your models here.

class adminYazı(admin.ModelAdmin):
    list_display = ["Name", "Surname", "yayinTarihi"]
    list_filter = ["yayinTarihi"]
    search_fields = ["Name", "Surname"]
    class Meta:
        model = yazı

admin.site.register(yazı,adminYazı)