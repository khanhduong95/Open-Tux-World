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
    image = scene.addObject(string,own,0)
    image.setParent(own,0,1)
    if item == 3:
        image.worldScale = [0.143*2, 0.043*2, 0.065*2]
    else:
        image.worldScale = [0.197, 0.197, 0.197]

def generate(cont, own, item, amount, scene): #generate collectible items
    new = scene.addObject("collect_item",own,0)
    new.worldPosition = own.worldPosition
    new["item"] = item
    new["amount"] = amount
    create_image(new, item, scene)

def main(cont):
    own = cont.owner

    try:
        if own.getDistanceTo(scene.objects["Cube"]) > common.AI_MAX_DISTANCE:
            own.endObject()
    except:
        pass
    
    col = cont.sensors["collect"]
    item = own["item"]
    amount = own["amount"]
    if col.positive and not col.hitObject["death"]:
        target = col.hitObject
        if item == 1 and target["snow"] < 30:
            if target["snow"] + amount >= 30:
                target["snow"] = 30
            else:
                target["snow"] += amount
            own.endObject()
        elif item == 2 and target["ice"] < 30:
            if target["ice"] + amount >= 30:
                target["ice"] = 30
            else:
                target["ice"] += amount
            own.endObject()
        elif item == 3 and target["fish"] < 30:
            if target["fish"] + amount >= 30:
                target["fish"] = 30
            else:
                target["fish"] += amount
            own.endObject()
