from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

import json
import os.path

# Create your views here.
def item(request, id):
    # replace with DB call
    filepath = os.path.join("items", str(id) + ".json")
    print(os.path.abspath(filepath))

    content = json.loads(open(filepath).read())

    #replace with DB call
    itemdata = json.loads(open("itemdata.json", "rb").read().decode())

    content.update(itemdata[str(content["item"])])

    # some prettyfying which will go to parser probably

    content["icon"] = "icons/" + content["icon"].replace(".", "/") + ".jpg"

    # result = json.dumps(content, indent=4, sort_keys=True)


    template = loader.get_template("item/tooltip.html")
    return HttpResponse(template.render(content))