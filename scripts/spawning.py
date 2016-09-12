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
        if not own["spawn_AI"] and AI_count <= 5:
            new_AI = scene.addObject("AI_penguin",own,0)
            own["spawn_AI"] = True
    elif 100 <= dist_cube < 200:
        if not own["spawn_AI"] and AI_count < 2:
            scene.addObject("AI_penguin",own,0)
            own["spawn_AI"] = True
    else:
        own["spawn_AI"] = False

def player_terrain(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    for obj in scene.objects:
        if "terrain_spawner" in obj:
            dist = own.worldPosition - obj.worldPosition
            if -1000 < dist.x < 1000 and -1000 < dist.y < 1000:
                if not obj["spawn_image"]:
                    image = scene.addObject(obj.name+"_image",obj,0)
                    image.setParent(obj,1,0)
                    obj["spawn_image"] = True
                if obj.getDistanceTo(own) >= 500:
                    if obj["spawn_physics"]:
                        obj.children[obj.name+"_physics"].endObject()
                        obj["spawn_physics"] = False
                elif not obj["spawn_physics"]:
                    physics = scene.addObject(obj.name+"_physics",obj,0)
                    physics.setParent(obj,1,0)
                    if "house" in obj:
                        physics_child = scene.addObject(obj.name+"_physics.001",physics,0)

                    else:
                        physics_child = scene.addObject(obj.name+"_physics",physics,0)
                        physics_child.worldPosition.z -= 0.03

                    physics_child.setParent(physics,0,0)
                    obj["spawn_physics"] = True

            elif obj["spawn_image"]:
                obj.children[obj.name+"_image"].endObject()
                obj["spawn_image"] = False
