from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.template import loader

from django.http import *
from .models import *
from .forms  import *
from item.models import Item
from achievement.models import Achievement

from datetime import datetime

import json

@csrf_exempt
@require_POST
def upload(request):
    print(request.body)
    data = request.body.decode()

    try:
        data = json.loads(data)
    except Exception:
        raise Http404("Not a valid JSON")

    server = get_object_or_404(Server, id = data["serverId"])
    
    player, created = Player.objects.get_or_create(
        pid = int(data["playerId"]), 
        server = server, 
        defaults = {
            "name": data["playerName"]
        }
    )

    # if renamed
    player.name = data["playerName"]
    player.klass = data["class"]
    player.race = data["race"]
    player.gender = data["gender"]

    # check this
    if player.race == Race.POPORI and player.gender == Gender.FEMALE:
        player.race = Race.ELIN

    player.save()


    # TODO gearsets
    gear = Gear()
    gear.save()

    player.gearsets.add(gear)

    for item in data["items"]:
        try:
            slot = Slot(item["slot"])
        except ValueError:
            continue

        item = Item.create_from_json(item, server)
        gear[slot] = item

    gear.save()

    for ach in data["achievements"]:
        id = int(ach["id"])
        completed = datetime.fromtimestamp(int(ach["completed"]))

        Achievement.objects.get_or_create(
            player = player,
            data   = get_object_or_404(AchievementData, id = id),
            defaults = {
                "completed": completed
            }
        )

    return HttpResponse("OK")

def player(request, id):
    player = get_object_or_404(Player, id=id)

    return render(
        request, 
        "gear/player.html",
        {
            "player": player,
            "main": player.getAchievements()
        }
    )

def index(request):
    return render(
        request, 
        "gear/index.html",
        {
            "form": PlayerSearchForm()
        }
    )

def search(request):
    players = Player.objects.all()

    players = players.filter(name__startswith = request.GET.get("player", ""))

    server = request.GET.get("server", "")
    if server:
        players = players.filter(server__name = server)

    print(players)

    return render(
        request,
        "gear/player_search.html",
        {
            "form": PlayerSearchForm(initial = request.GET),
            "players": players
        }
    )


def gear(request, id):
    return render (
        request,
        "gear/gear.html",        
        {
            "gear": get_object_or_404(Gear, id=id),
        }
    )

def compare(request, p1=None, p2=None):
    if p2 is None:
        return render(
            request,
            "gear/compare_search.html",
            {
                "cplayer": get_object_or_404(Player, id=p1) if p1 is not None else None,
                "players": Player.objects.all()
            }
        )

    p1 = get_object_or_404(Player, id=p1)
    p2 = get_object_or_404(Player, id=p2)

    return render(
        request,
        "gear/compare.html",
        {
            "player": p1,
            "playerOther": p2,
            "comparison": p1.compareAchievements(p2)
        }
    )