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


    # make a custom field I guess later
    class Display:
        def __init__(self, parent):
            self.parent = parent

        @property 
        def race(self):
            race = Race(self.parent.race)

            if race == Race.POPORI and Gender(self.parent.gender) == Gender.FEMALE:
                return "Elin"

            return race.display_name()

        @property
        def gender(self):
            return Gender(self.parent.gender).display_name()

        @property
        def klass(self):
            return Klass(self.parent.klass).display_name()

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.display = Player.Display(self)
