from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from item.models import ItemData

import json
import os.path

# Create your views here.
def item(request, id):
    # replace with DB call
    filepath = os.path.join("items", str(id) + ".json")
    print(os.path.abspath(filepath))

    content = json.loads(open(filepath).read())

    #replace with DB call

    item_id = content["item"]
    itemdata = ItemData.objects.get(id = item_id)

    itemdata.icon = "item/" + itemdata.icon

    template = loader.get_template("item/tooltip.html")
    return HttpResponse(
        template.render({
            "itemdata": itemdata,
            "content" : content
        })
    )