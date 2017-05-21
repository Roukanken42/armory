from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)
admin.site.register(Achievement)

class AchievementDataAdmin(admin.ModelAdmin):
    search_fields = ["name"]

admin.site.register(AchievementData, AchievementDataAdmin)