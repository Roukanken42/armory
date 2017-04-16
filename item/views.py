from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from item.models import ItemData, Item

import json
import os.path

# Create your views here.
def item(request, id):
    item = Item.objects.get(id = id)

    template = loader.get_template("item/tooltip.html")
    
    return HttpResponse(
        template.render({
            "item": item,
        })
    )