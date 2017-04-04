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

    equipmentData = models.ForeignKey(
        "EquipmentData",
        models.SET_NULL,
        null = True
    )
    # discutable

    # "artisanable": false,
    # "unidentifiedItemGrade": 0,
    # "dismantlable": false,
    # "name": "service_item_01",
    # "obtainable": true,
    # "changeLook": false,

    # dropped - at least for now

    # links only ?

    # "linkCrestId": 0,
    # "linkCustomizingId": 0,
    # "linkLookInfoId": 0,
    # "linkPetAdultId": 0,
    # "linkPetOrbId": 0,
    # "linkSkillId": 60410500,

    # not usefull

    # slotLimit = models.IntegerField()         Ketoh says useless
    
    # "buyPrice": "10000",
    # "sellPrice": "1000",

    # "changeColorEnable": false,
    # "destroyable": true,
    # "extractLook": false,

    # "dropSilhouette": "Item_Drop.SM.Potion_SM",
    # "sortingNumber": 1101,
    # "masterpieceRate": 0.0,
    # "maxStack": 100,
    # "useOnlyTerritory": false,
    # "equipSound": "InterfaceSound.Equip_ItemCUE.Equip_NormalCue",
    # "dropSound": "InterfaceSound.Drop_ItemCUE.Drop_PotionCue",
    # "coolTime": 30,
    # "coolTimeGroup": 3,

class EquipmentData(models.Model):
    balance      = models.IntegerField(null=True) 
    crystalslots = models.IntegerField(null=True)       #countOfSlots
    defence      = models.IntegerField(null=True)       #def
    impact       = models.IntegerField(null=True) 
    attack       = models.IntegerField(null=True)       #minAtk / maxAtk
    
class Item(models.Model):
    type      = models.IntegerField()

    enchant   = models.IntegerField()
    itemLevel = models.IntegerField()
    feedstock = models.IntegerField()
    
    crystal1  = models.IntegerField()
    crystal2  = models.IntegerField()
    crystal3  = models.IntegerField()
    crystal4  = models.IntegerField()

    # "bonuses": []
