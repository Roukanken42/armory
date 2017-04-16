from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from item.models import ItemData, Item

import json
import os.path

# Create your views here.
def item(request, id):
    item = Item.objects.get(id = id)

    # itemdata.enchant = item.enchant
    # itemdata.itemLevel = item.itemLevel
    # itemdata.feedstock = item.feedstock

    # crystals = []
    # for crystal in ["crystal1", "crystal2", "crystal3", "crystal4"]:
    #     crystal_id = getattr(item, crystal)
        
    #     if crystal_id == 0:
    #         continue

    #     crystals += [ItemData.objects.get(id = crystal_id)]
    
    # itemdata.crystals = crystals
    # itemdata.bonuses = item.bonuses

    template = loader.get_template("item/tooltip.html")
    
    return HttpResponse(
        template.render({
            "item": item,
        })
    )