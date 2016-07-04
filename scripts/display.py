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
from bge import logic

def get_scene(string):
    scenes = logic.getSceneList()
    for i in scenes:
        if i.name == string:
            return i

def amount(cont):
    own = cont.owner
    try:
        cube = get_scene("Scene").objects.from_id(logic.globalDict.get("player_id"))
        snow = cube["snow"]
        ice = cube["ice"]
        fish = cube["fish"]
        if own.parent["item"] == 1:
            own.text = str(snow)
        elif own.parent["item"] == 2:
            own.text = str(ice)
        elif own.parent["item"] == 3:
            own.text = str(fish)
        else:
            own.text = ""
    except:
        return

def item(cont):
    own = cont.owner
    item = own["item"]
    scene = logic.getCurrentScene()
    try:
        new = get_scene("Scene").objects.from_id(logic.globalDict.get("player_id"))["item"]
        if item != new:
            if item == 1:
                own.children["snow_ball"].endObject()
            elif item == 2:
                own.children["ice_cube"].endObject()
            elif item == 3:
                own.children["fish"].endObject()
            if new == 1:
                snow = scene.addObject("snow_ball", own, 0)
                snow.setParent(own, 0, 1)
                snow.worldScale = [0.19,0.19,0.19]
            elif new == 2:
                ice = scene.addObject("ice_cube", own, 0)
                ice.setParent(own, 0, 1)
                ice.worldScale = [0.19,0.19,0.19]
            elif new == 3:
                fish = scene.addObject("fish", own, 0)
                fish.setParent(own, 0, 1)
                #fish.alignAxisToVect([0.0,1.0,0.0],2,1.0)
                fish.alignAxisToVect([0.0,0.0,-1.0],1,1.0)
                fish.worldScale = [0.143*1.5,0.043*1.5,0.065*1.5]
            own["item"] = new
    except:
        return

def health(cont):
    own = cont.owner
    try:
        health = get_scene("Scene").objects.from_id(logic.globalDict.get("player_id"))["health"]
        if health <= 0:
            own.worldScale = [0, 0.05, 0.05]
        else:
            own.worldScale = [health/100, 0.05, 0.05]
    except:
        return
