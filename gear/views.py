from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.template import loader

from django.http import *
from .models import *
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
    if player.name != data["playerName"]:
        player.name = data["playerName"]
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
    ...

def gear(request, id):
    gear = get_object_or_404(Gear, id=id)

    for slot in gear.gear_item_set.all().select_related():
        print(slot.slot, slot.item)

    template = loader.get_template("gear/gear.html")

    return HttpResponse(
        template.render({
            "gear": gear,
            "slot": Slot
        })
    )