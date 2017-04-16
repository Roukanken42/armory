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


positions = {
    Slot.WEAPON:       (69, 93),
    Slot.ARMOR:        (338, 93),
    Slot.BOOTS:        (69, 178),
    Slot.GLOVES:       (338, 178),
    Slot.NECKLACE:     (160, 80),
    Slot.INNERWEAR:    (203, 151),
    Slot.BELT:         (203, 224),
    Slot.LEFT_RING:    (58, 263),
    Slot.RIGHT_RING:   (349, 263),
    Slot.LEFT_EARING:  (58, 9),
    Slot.RIGHT_EARING: (349, 9),
    Slot.BROOCH:       (247, 80),
    Slot.CIRCLET:      (137, 9),
}

crystal_positions = {
    Slot.WEAPON:        ((8, 72), (8, 118), (8, 164), (8, 210)),
    Slot.ARMOR:         ((410, 72), (410, 118), (410, 164), (410, 210)),
    Slot.RIGHT_EARING:  ((410, 8),),
    Slot.LEFT_EARING:   ((8, 8),),
    Slot.RIGHT_RING:    ((410, 274),),
    Slot.LEFT_RING:     ((8, 274),),
}

def gear(request, id):
    return HttpResponse(
        request,
        "gear/gear.html",        
        {
            "gear": get_object_or_404(Gear, id=id),
            "Slot": Slot,
            "positions": positions,
            "crystal_positions": crystal_positions
        }
    )