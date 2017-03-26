from django.db import models

# Create your models here.
class ItemData(models.Model):                   # comments for parsing purposes
    type = models.IntegerField()                # id
    name = models.CharField(max_length=200)     # string
    tooltip = models.CharField(max_length=500)  # toolTip
    icon = models.CharField(max_length=200)     
    
    tradable = models.BooleanField()
    warehouseStorable = models.BooleanField()
    guildWarehouseStorable = models.BooleanField()
    storeSellable = models.BooleanField()
    enchantEnable = models.BooleanField()

    boundType = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    combatItemType = models.CharField(max_length=20)
    requiredEquipmentType = models.CharField(max_length=20)

    level = models.IntegerField()
    rank = models.IntegerField()
    rareGrade = models.IntegerField()

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
    # "linkEquipmentId": 0,
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
