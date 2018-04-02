#
#    Copyright (C) 2016 Dang Duong
#
#    This file is part of Open Tux World.
#
#    Open Tux World is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Open Tux World is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Open Tux World.  If not, see <http://www.gnu.org/licenses/>.
#
from scripts import common

logic = common.logic
scene = common.scene

def create_image(own, item, scene): #create an image of each collectible item
    if item == 1:
        string = "snow_ball"
    elif item == 2:
        string = "ice_cube"
    elif item == 3:
        string = "fish"
    image = scene.addObject(string, own, 0)
    image.setParent(own,0,1)
    if item == 3:
        image.worldScale = [0.143*2, 0.043*2, 0.065*2]
    else:
        image.worldScale = [0.197, 0.197, 0.197]

def generate(cont, own, item, amount, scene): #generate collectible items
    new = scene.addObject("collect_item", own, common.ITEM_COLLECT_EXPIRE)
    new.worldPosition = own.worldPosition
    new["item"] = item
    new["amount"] = amount
    create_image(new, item, scene)

def main(cont):
    own = cont.owner
    
    col = cont.sensors["collect"]
    item = own["item"]
    amount = own["amount"]

    if col.positive and col.hitObject["health"] > 0:
        target = col.hitObject
        if item == 1 and target["snow"] < common.ITEM_MAX_COUNT:
            if target["snow"] + amount >= common.ITEM_MAX_COUNT:
                target["snow"] = common.ITEM_MAX_COUNT
            else:
                target["snow"] += amount
            own.endObject()
        elif item == 2 and target["ice"] < common.ITEM_MAX_COUNT:
            if target["ice"] + amount >= common.ITEM_MAX_COUNT:
                target["ice"] = common.ITEM_MAX_COUNT
            else:
                target["ice"] += amount
            own.endObject()
        elif item == 3 and target["fish"] < common.ITEM_MAX_COUNT:
            if target["fish"] + amount >= common.ITEM_MAX_COUNT:
                target["fish"] = common.ITEM_MAX_COUNT
            else:
                target["fish"] += amount
            own.endObject()

    for player_id in logic.globalDict["player_list"]:
        try:
            if own.getDistanceTo(scene.objects.from_id(player_id).children["player_loc"]) < common.ITEM_MAX_DISTANCE:
                return
        except:
            continue
    
    own.endObject()
