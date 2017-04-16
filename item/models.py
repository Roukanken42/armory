from django.db import models

# Create your models here.
class ItemData(models.Model):                   # comments for parsing purposes
    name = models.CharField(max_length=200)     # string
    tooltip = models.CharField(max_length=1000)  # toolTip
    icon = models.CharField(max_length=200)     
    
    tradeable = models.BooleanField(default=True)
    warehouseStorable = models.BooleanField(default=True)
    guildWarehouseStorable = models.BooleanField(default=True)
    storeSellable = models.BooleanField(default=True)
    enchantable = models.BooleanField(default=False)

    boundType = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    combatItemType = models.CharField(max_length=40)
    requiredEquipmentType = models.CharField(max_length=20)

    level = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    rarity = models.IntegerField(null=True)          #rareGrade

    equipment = models.ForeignKey(
        "EquipmentData",
        models.SET_NULL,
        null = True
    )

    passivity = models.ManyToManyField("Passivity")

    def __str__(self):
        return "<" + self.name + ">"


class EquipmentData(models.Model):
    balance      = models.IntegerField(null=True) 
    crystalslots = models.IntegerField(null=True)       #countOfSlots
    defence      = models.IntegerField(null=True)       #def
    impact       = models.IntegerField(null=True) 
    attack       = models.IntegerField(null=True)       #minAtk / maxAtk
    

class Item(models.Model):
    data      = models.ForeignKey(ItemData)
    server    = models.ForeignKey("gear.Server")

    uid       = models.IntegerField()

    enchant   = models.IntegerField(null = True)
    itemLevel = models.IntegerField(null = True)
    feedstock = models.IntegerField(null = True)
    
    crystal1  = models.ForeignKey(ItemData, related_name="crystal1", null = True)
    crystal2  = models.ForeignKey(ItemData, related_name="crystal2", null = True)
    crystal3  = models.ForeignKey(ItemData, related_name="crystal3", null = True)
    crystal4  = models.ForeignKey(ItemData, related_name="crystal4", null = True)

    bonuses   = models.ManyToManyField("Passivity")

    def __str__(self):
        return str(self.data)

    def crystals(self):
        return [Item(data = x, server = self.server, uid = 0) for x in [self.crystal1, self.crystal2, self.crystal3, self.crystal4] if x != None]

    @classmethod
    def create_from_json(self, data, server):
        itemdata = ItemData.objects.get(id = data["item"])
        item, created = Item.objects.get_or_create(uid = data["uid"], server = server, data = itemdata)

        for name in item.__dict__.keys():
            if name.startswith("_") or name in ["id", "uid", "data_id", "server_id"]:
                continue

            if name.endswith("_id"):
                value = data[name[:-3]]

                if value == 0: 
                    value = None
            else:
                value = data[name]

            setattr(item, name, value)

        bonuses = [
            Passivity.objects.get(id = bonus)
            for bonus in data["bonuses"]
        ]

        item.bonuses.add(*bonuses)
        item.save()

        return item

class Passivity(models.Model):
    name = models.CharField(max_length=200)     # string
    tooltip = models.CharField(max_length=1000)  # toolTip
