from django.shortcuts import render, get_object_or_404

from . import models
from gear.models import Player


# Create your views here.

# def getAchievements():
#     top = models.Category.objects.get(id=42)
#     main = list(top.subcategories.all())

#     for cat in main:
#         for sub in cat.subcategories.all():
#             # print(sub.achievementdata_set.all())
#             pass

def achievement(request, id):
    player = get_object_or_404(Player, id=id)
    # achievements = player.getAchievements()

    return render(
        request, 
        "achievement/achievement.html",
        {
            "player": player,
        }
    )
