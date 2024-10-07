from django.contrib import admin
from .models import *

# Register your models here.

from .models import outt
# Register your models here.
admin.site.register(outt)

# to display as name not as object
class outtAdmin(admin.ModelAdmin):
    list_display=["name","plf"]