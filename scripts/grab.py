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

def change_item(own, new, current):
    scene = logic.getCurrentScene()
    try:
        if current == 1:
            own.children["snow_ball"].endObject()
        elif current == 2:
            own.children["ice_cube"].endObject()
        elif current == 3:
            own.children["fish"].endObject()
    except:
        pass
    if new == 1:
        snow = scene.addObject("snow_ball",own,0)
        snow.setParent(own,0,1)
        snow.worldScale = [0.197,0.197,0.197]
    elif new == 2:
        ice = scene.addObject("ice_cube",own,0)
        ice.setParent(own,0,1)
        ice.worldScale = [0.197,0.197,0.197]
    elif new == 3:
        fish = scene.addObject("fish",own,0)
        fish.setParent(own,0,1)
        fish.worldScale = [0.143*2,0.043*2,0.065*2]

def main(cont):
    own = cont.owner
    new = own.parent.parent["item"] #new item
    current = own["current"] #current item
    if own.parent.parent["death"]:
        change_item(own, 0, current)
        own.state = logic.KX_STATE2
    elif new != current:
        change_item(own, new, current)
    own["current"] = new
