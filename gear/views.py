from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.template import loader

from django.http import *
from .models import *
from .forms  import *
from item.models import Item

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
    return HttpResponse("OK")

def player(request, id):
    return render(
        request, 
        "gear/player.html",
        {
            "player": get_object_or_404(Player, id=id),
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