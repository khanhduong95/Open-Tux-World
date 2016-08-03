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

def AI(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    AI_list = []
    for obj in scene.objects:
        if "AI" in obj and own.getDistanceTo(obj) < 100 and obj not in AI_list:
            AI_list.append(obj)
    AI_count = len(AI_list)
    try:
        cube = scene.objects["Cube"]
        dist_cube = own.getDistanceTo(cube)
        dist_for_dir = own.getDistanceTo(cube.children["camera_track"].children["forward_dir"])
    except:
        return

    if 50 < dist_cube < 100 and dist_cube < dist_for_dir:
        if not own["spawn"] and AI_count <= 5:
            scene.addObject("AI_penguin",own,0)
            own["spawn"] = True
    elif 100 <= dist_cube < 200:
        if not own["spawn"] and AI_count < 2:
            scene.addObject("AI_penguin",own,0)
            own["spawn"] = True
    else:
        own["spawn"] = False

def terrain(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    try:
        player = scene.objects["player_loc"]
    except:
        return

    if own.getDistanceTo(player) >= 500:
        if own["spawn_physics"]:
            own.children[own.name+"_physics"].endObject()
            own["spawn_physics"] = False
    elif not own["spawn_physics"]:
        physics = scene.addObject(own.name+"_physics",own,0)
        physics.setParent(own,1,0)
        physics_child = scene.addObject(own.name+"_physics",physics,0)
        physics_child.worldPosition.z -= 0.03
        physics_child.setParent(physics,0,0)
        own["spawn_physics"] = True

    dist = own.worldPosition - player.worldPosition
    if (dist.x >= 1000 and dist.y >= 1000) or (dist.x <= -1000 and dist.y <= -1000):
        if own["spawn_image"]:
            own.children[own.name+"_image"].endObject()
            own["spawn_image"] = False
            own.state = logic.KX_STATE1
    elif not own["spawn_image"]:
        image = scene.addObject(own.name+"_image",own,0)
        image.setParent(own,1,0)
        own["spawn_image"] = True

def player_terrain(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    for obj in scene.objects:
        if "terrain_spawner" in obj:
            dist = own.worldPosition - obj.worldPosition
            if (dist.x < 1000 and dist.x > -1000) or (dist.y < 1000 and dist.y > -1000):
                obj.state = logic.KX_STATE2
