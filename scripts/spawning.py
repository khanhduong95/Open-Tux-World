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

    own_terrain_key_name = "terrain_" + physics_or_image + "_key"
    if key != own[own_terrain_key_name]:
        old_key = own[own_terrain_key_name]
        terrain_player_list_name = "terrain_" + physics_or_image + "_player_list"
        try:
            global_dict[terrain_player_list_name][key].append(own_id)
        except:
            global_dict[terrain_player_list_name][key] = [own_id]

        if old_key != "":
            global_dict[terrain_player_list_name][old_key].remove(own_id)
            if not global_dict[terrain_player_list_name][old_key]:
                global_dict[terrain_player_list_name].pop(old_key, None)
                if own_is_physics:
                    global_dict["terrain_physics_dict"].pop(old_key, None)
                else:
                    global_dict["terrain_image_dict"].discard(old_key)

        own[own_terrain_key_name] = key

    terrain_dict_name = "terrain_" + physics_or_image + "_dict"
    if key in global_dict[terrain_dict_name]:
        if own_is_physics:
            for terrain_name in global_dict[terrain_dict_name][key]:
                spawn_AI(own, scene.objects[terrain_name])
        return

    loc_dir = os.path.join(dict_dir, physics_or_image, key, "")        
        
    for file in os.listdir(loc_dir):
        if file.endswith(".json"):
            with open(loc_dir + file, "r") as json_file:
                json_data = json.load(json_file)
                if own_is_physics:
                    global_dict["terrain_physics_dict"][key] = json_data
                else:
                    global_dict["terrain_image_dict"].add(key)
                    
                for terrain_name in json_data:
                    if terrain_name not in global_dict["active_terrain_list"]:
                        global_dict["active_terrain_list"].add(terrain_name)
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
