from django.db import models
from item.models import Item

from common.utils import ChoiceEnum
from enum import Enum

class Slot(ChoiceEnum):
    WEAPON = 1
    ARMOR  = 3
    GLOVES = 4
    BOOTS  = 5

    LEFT_EARING  = 6
    RIGHT_EARING = 7
    LEFT_RING    = 8
    RIGHT_RING   = 9
    NECKLACE     = 10

    INNERWEAR = 11
    BELT      = 19
    BROOCH    = 20    

class Gear_Item(models.Model):
    item    = models.ForeignKey(Item,   models.CASCADE)
    gearset = models.ForeignKey("Gear", models.CASCADE)
    slot    = models.IntegerField(choices = Slot.choices())


class Gear(models.Model):
    timestamp = models.DateField(auto_now=True)
    items = models.ManyToManyField(Item, through=Gear_Item)

    def get(self, slot):
        if isinstance(slot, Enum):
            slot = slot.value

        return self.items.get(slot=slot)

class Server(models.Model):
    id = models.IntegerField(primary_key=True)
    name   = models.CharField(max_length=30)
    region = models.CharField(max_length=2)

    def __str__(self):
        return "<Server {0.name}: id={0.id}, region={0.region}>".format(self)


class Player(models.Model):
    pid     = models.IntegerField()
    name   = models.CharField(max_length=30)
    server = models.ForeignKey(Server, models.CASCADE)

    gearsets = models.ManyToManyField(Gear)

    def __str__(self):
        return "<Player {0.name}: pid={0.pid}, server={0.server.name}>".format(self)

