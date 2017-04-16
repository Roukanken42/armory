from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from item.models import ItemData, Item


# Create your views here.
def item(request, id):
    return render (
        request,
        "item/tooltip.html",
        {
            "item": get_object_or_404(Item, id = id),
        }
    )