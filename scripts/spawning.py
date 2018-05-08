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
import os
import json

logic = common.logic
scene = common.scene
global_dict = logic.globalDict
terrain_spawner = scene.objects["terrain_spawner"]

def spawn_AI(own, terrain):
    AI_count = len(global_dict["AI_list"])

    if AI_count <= common.AI_MAX_COUNT:
        dist_player = terrain.getDistanceTo(own)
        dist_cam = terrain.getDistanceTo(own.parent.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"])
        if common.AI_SPAWN_MIN_DISTANCE < dist_player < common.AI_SPAWN_MAX_DISTANCE and dist_player > dist_cam:
            terrain_spawner.worldPosition = terrain.worldPosition
            terrain_spawner.worldPosition[2] += 1
            AI = scene.addObject("AI_penguin", terrain_spawner, 0).groupMembers["AI_Cube"]
            # print("AI " + str(id(AI)) + " spawned")
            vec = AI.worldPosition - own.worldPosition
            AI.alignAxisToVect([vec.x, vec.y, 0], 0, 1)#point to player

def add_player_to_terrain(player_id, terrain_name):
    if player_id not in global_dict["active_terrain_list"][terrain_name]:
        global_dict["active_terrain_list"][terrain_name].append(player_id)

def check_near_terrains(own, own_id, own_pos, own_is_physics):
    dict_dir = global_dict["terrain_dict_dir"]
    if own_is_physics:
        physics_or_image = "physics"
        max_distance = common.TERRAIN_PHYSICS_MAX_DISTANCE
        key = str(int(own_pos[0] / max_distance)) + "_" + str(int(own_pos[1] / max_distance)) + "_" + str(int(own_pos[2] / max_distance))
    else:
        physics_or_image = "image"
        max_distance = common.TERRAIN_IMAGE_MAX_DISTANCE
        key = str(int(own_pos[0] / max_distance)) + "_" + str(int(own_pos[1] / max_distance))

    terrain_dict_name = "terrain_" + physics_or_image + "_dict"
    if key in global_dict[terrain_dict_name]:
        for terrain_name in global_dict[terrain_dict_name][key]:
            add_player_to_terrain(own_id, terrain_name)
            if own_is_physics:
                spawn_AI(own, scene.objects[terrain_name])
        return

    loc_dir = os.path.join(dict_dir, physics_or_image, key, "")        
        
    for file in os.listdir(loc_dir):
        if file.endswith(".json"):
            with open(loc_dir + file, "r") as json_file:
                json_data = json.load(json_file)        
                global_dict[terrain_dict_name][key] = json_data
                for terrain_name in json_data:
                    try:
                        add_player_to_terrain(own_id, terrain_name)
                    except:
                        global_dict["active_terrain_list"][terrain_name] = [own_id]
                        terrain_lib_loader = scene.addObject("terrain_lib_loader", terrain_spawner, 0)
                        terrain_lib_loader["physics"] = own_is_physics
                        terrain_lib_loader["terrain_name"] = terrain_name
                        terrain_lib_loader.state = logic.KX_STATE2
            
def main(cont):
    own = cont.owner
    own_id = id(own)
    own_pos = own.worldPosition    
    check_near_terrains(own, own_id, own_pos, False)
    check_near_terrains(own, own_id, own_pos, True)
