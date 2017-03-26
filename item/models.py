from django.db import models

# Create your models here.
class ItemData(models.Model):                   #for parsing purposes
    type = models.IntegerField()                #id
    name = models.CharField(max_length=200)     #string
    tooltip = models.CharField(max_length=500)  #toolTip


    # "artisanable": false,
    # "boundType": "None",
    # "buyPrice": "10000",
    # "category": "combat",
    # "changeColorEnable": false,
    # "changeLook": false,
    # "combatItemType": "DISPOSAL",
    # "coolTime": 30,
    # "coolTimeGroup": 3,
    # "destroyable": true,
    # "dismantlable": false,
    # "dropSilhouette": "Item_Drop.SM.Potion_SM",
    # "dropSound": "InterfaceSound.Drop_ItemCUE.Drop_PotionCue",
    # "enchantEnable": false,
    # "equipSound": "InterfaceSound.Equip_ItemCUE.Equip_NormalCue",
    # "extractLook": false,
    # "guildWarehouseStorable": false,
    # "icon": "Icon_Items.Artisan_Potion_Tex",
    # "id": 1,
    # "level": 1,
    # "linkCrestId": 0,
    # "linkCustomizingId": 0,
    # "linkEquipmentId": 0,
    # "linkLookInfoId": 0,
    # "linkPetAdultId": 0,
    # "linkPetOrbId": 0,
    # "linkSkillId": 60410500,
    # "masterpieceRate": 0.0,
    # "maxStack": 100,
    # "name": "service_item_01",
    # "obtainable": true,
    # "rank": 0,
    # "rareGrade": 1,
    # "requiredEquipmentType": "NO_COMBAT",
    # "sellPrice": "1000",
    # "slotLimit": 0,
    # "sortingNumber": 1101,
    # "storeSellable": false,
    # "tradable": false,
    # "unidentifiedItemGrade": 0,
    # "warehouseStorable": false


    # "useOnlyTerritory": false,
