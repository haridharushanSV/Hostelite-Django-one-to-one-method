from django.contrib import admin

# Register your models here.
from .models import outp
# Register your models here.
@admin.register(outp)
class outtAdmin(admin.ModelAdmin):
    list_display=["name","plf"]