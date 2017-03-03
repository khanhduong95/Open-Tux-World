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
from scripts import common_functions as cf
from bge import logic

AI_MAX_DISTANCE = 100
AI_CLOSE_DISTANCE = 20
AI_MAX_COUNT = 10
AI_CLOSE_COUNT = 2
TERRAIN_GROUP_MAX_DISTANCE = 2500
TERRAIN_CHILD_GROUP_MAX_DISTANCE = 1500
TERRAIN_CHILD_CHILD_GROUP_MAX_DISTANCE = 1500
TERRAIN_MAX_DISTANCE = 500
TERRAIN_PHYSICS_MAX_DISTANCE = 250

scene = logic.getCurrentScene()

def terrain_main(cont):
    try:
        player = scene.objects["Cube"]
    except:
        return
    own = cont.owner
    dist = own.worldPosition - player.worldPosition
    if -TERRAIN_MAX_DISTANCE > dist.x or dist.x > TERRAIN_MAX_DISTANCE or -TERRAIN_MAX_DISTANCE > dist.y or dist.y > TERRAIN_MAX_DISTANCE:
        own.endObject()

def terrain_physics_main(cont):
    try:
        player = scene.objects["Cube"]
    except:
        return
    own = cont.owner
    dist = own.getDistanceTo(player)
    if dist > TERRAIN_PHYSICS_MAX_DISTANCE:
        own.endObject()
