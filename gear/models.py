from django.db import models
from item.models import Item

from common.utils import *
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
    CIRCLET   = 12
    BELT      = 19
    BROOCH    = 20

class Race(ChoiceEnum):
    HUMAN       = 0
    HIGH_ELF    = 1
    AMAN        = 2
    CASTANIC    = 3
    POPORI      = 4
    BARAKA      = 5

class Gender(ChoiceEnum):
    FEMALE  = 0
    MALE    = 1

class Klass(ChoiceEnum):
    WARRIOR     = 1
    LANCER      = 2
    SLAYER      = 3
    BERSERKER   = 4
    SORCERER    = 5
    ARCHER      = 6
    PRIEST      = 7
    MYSTIC      = 8
    REAPER      = 9
    GUNNER      = 10
    BRAWLER     = 11
    NINJA       = 12
    VALKYRIE    = 13


@make_model
@add_enum_field(Slot, lambda enum: models.ForeignKey(Item, related_name=enum.name.lower(), null=True))
class Gear:
    timestamp = models.DateField(auto_now=True)

    def __getitem__(self, x):
        return getattr(self, x.name.lower())

    def __setitem__(self, x, value):
        return setattr(self, x.name.lower(), value)

    def all(self):
        for x in Slot.all():
            yield (x, self[x])

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

    race   = models.IntegerField(choices =   Race.choices(), null=True)
    gender = models.IntegerField(choices = Gender.choices(), null=True)
    klass  = models.IntegerField(choices =  Klass.choices(), null=True)

    gearsets = models.ManyToManyField(Gear)

    def __str__(self):
        return "<Player {0.name}: pid={0.pid}, server={0.server.name}>".format(self)

