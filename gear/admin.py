from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Gear)
admin.site.register(Server)
admin.site.register(Player)
admin.site.register(Gear_Item)