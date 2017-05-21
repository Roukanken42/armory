from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    search_fields = ["data__name", "player__name"]


@admin.register(AchievementData)
class AchievementDataAdmin(admin.ModelAdmin):
    search_fields = ["name"]

