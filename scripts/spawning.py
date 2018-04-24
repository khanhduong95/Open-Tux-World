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

def load_terrain_dict(key):
    dict_dir = global_dict["terrain_dict_dir"]
    global_dict["terrain_dict"][key] = {"data": {}, "image": [], "physics": {}, "ready": 0}
    loc_dir = os.path.join(dict_dir, key, "")
    for file in os.listdir(loc_dir):
        if file.endswith("_dict.json"):
            with open(loc_dir + file, "r") as json_file:
                json_data = json.load(json_file)
                global_dict["terrain_dict"][key]["image"].extend(json_data["image"])
                for k, v in json_data["physics"].items():
                    if k in global_dict["terrain_dict"][key]["physics"]:
                        global_dict["terrain_dict"][key]["physics"][k].extend(v)
                    else:
                        global_dict["terrain_dict"][key]["physics"][k] = v
                global_dict["terrain_dict"][key]["data"].update(json_data["data"])

def check_near_terrains(own, own_id, own_pos, own_is_physics, image_key):
    if own_is_physics:
        max_distance = common.TERRAIN_PHYSICS_MAX_DISTANCE
        x = str(int(own_pos[0] / max_distance))
        y = str(int(own_pos[1] / max_distance))
        z = str(int(own_pos[2] / max_distance))
        key = x + "_" + y + "_" + z
        physics_or_image = "physics"
        terrain_dict = global_dict["terrain_dict"][image_key][physics_or_image][key]
    else:
        key = image_key
        physics_or_image = "image"       
        terrain_dict = global_dict["terrain_dict"][image_key][physics_or_image]

    terrain_data = global_dict["terrain_dict"][image_key]["data"]
    terrain_list_name = "terrain_" + physics_or_image + "_list"
    for terrain_name in terrain_dict:
        terrain = terrain_data[terrain_name]
        terrain_pos = terrain["location"]
        try:
            terrain_info = global_dict[terrain_list_name][terrain_name]
            if own_id not in terrain_info["players"]:
                global_dict[terrain_list_name][terrain_name]["players"].append(own_id)

            if own_is_physics:
                spawn_AI(own, scene.objects.from_id(terrain_info["id"]))
            
        except:
            terrain_spawner.worldPosition = terrain_pos
            new_terrain = scene.addObject(terrain_name, terrain_spawner, 0)
            terrain_loc = scene.addObject("terrain_loc", terrain_spawner, 0)
            terrain_loc["terrain_name"] = terrain_name
            if own_is_physics:
                for terrain_mem in new_terrain.groupMembers:                
                    terrain_mem.setParent(terrain_loc, 0, 0)
                terrain_loc["physics"] = True
            new_terrain.setParent(terrain_loc, 0, 0)
            terrain_id = id(terrain_loc)

            global_dict[terrain_list_name][terrain_name] = {"players": [own_id], "id": terrain_id}
            print("Terrain " + physics_or_image + " " + terrain_name + " " + str(terrain_id) + " added")

            if not own_is_physics:
                continue
            
            try:
                house_physics = new_terrain.children["house_physics"]
            except:
                for house in terrain["houses"]:
                    terrain_spawner.worldPosition = house["location"]
                    house_physics = scene.addObject("house_physics", terrain_spawner, 0)
                    house_physics.applyRotation(house["rotation"], False)
                    house_physics.setParent(new_terrain, 0, 0)

def main(cont):
    own = cont.owner
    own_id = id(own)
    own_pos = own.worldPosition
    max_distance = common.TERRAIN_IMAGE_MAX_DISTANCE
    x = int(own_pos[0] / max_distance)
    y = int(own_pos[1] / max_distance)
    key = str(x) + "_" + str(y)
    if key not in global_dict["terrain_dict"]:
        load_terrain_dict(key)
        for image in global_dict["terrain_dict"][key]["image"]:
            terrain_lib_loader = scene.addObject("terrain_lib_loader", terrain_spawner, 0)
            terrain_lib_loader["key"] = key
            terrain_lib_loader["lib_name"] = image
            terrain_lib_loader.state = logic.KX_STATE2
    if global_dict["terrain_dict"][key]["ready"] == len(global_dict["terrain_dict"][key]["image"]):
        check_near_terrains(own, own_id, own_pos, False, key)
        check_near_terrains(own, own_id, own_pos, True, key)
