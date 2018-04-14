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
global_dict = logic.globalDict
terrain_spawner = scene.objects["terrain_spawner"]

# def close_distance(own_pos, terrain_loc, dist_const):
#     return common.getDistance([terrain_loc[0] - own_pos[0], terrain_loc[1] - own_pos[1], terrain_loc[2] - own_pos[2]]) < dist_const

def spawn_AI(own, terrain):
    AI_count = len(global_dict["AI_list"])

    if AI_count <= common.AI_MAX_COUNT:
        dist_player = terrain.getDistanceTo(own)
        dist_cam = terrain.getDistanceTo(own.parent.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"])
        if common.AI_SPAWN_MIN_DISTANCE < dist_player < common.AI_SPAWN_MAX_DISTANCE and dist_player > dist_cam:
            terrain_spawner.worldPosition = terrain.worldPosition
            terrain_spawner.worldPosition[2] += 1
            AI = scene.addObject("AI_penguin", terrain_spawner, 0).groupMembers["AI_Cube"]
            print("AI " + str(id(AI)) + " spawned")
            vec = AI.worldPosition - own.worldPosition
            AI.alignAxisToVect([vec.x, vec.y, 0], 0, 1)#point to player

def check_near_terrains(own, own_id, own_pos, own_is_physics, max_distance):
    x = str(own_pos[0] // max_distance)
    y = str(own_pos[1] // max_distance)
    key = x+"_"+y
    physics_or_image = "physics" if own_is_physics else "image"

    if own_is_physics:
        z = str(own_pos[2] // max_distance)
        key += "_"+z
    
    terrain_list_name = "terrain_" + physics_or_image + "_list"
    for terrain in global_dict["terrain_dict"][physics_or_image][key]:
        terrain_name = terrain["name"]
        try:
            terrain_info = global_dict[terrain_list_name][terrain_name]
        except:
            terrain_info = global_dict[terrain_list_name][terrain_name] = {}

        terrain_pos = terrain["location"]
        terrain_x = str(terrain_pos[0] // max_distance)
        terrain_y = str(terrain_pos[1] // max_distance)
        terrain_key = terrain_x + "_" + terrain_y

        if own_is_physics:
            terrain_z = str(terrain_pos[2] // max_distance)
            terrain_key += "_" + terrain_z
            
        try:
            if own_id not in terrain_info[terrain_key]["players"]:
                global_dict[terrain_list_name][terrain_name][terrain_key]["players"].append(own_id)

            spawn_AI(own, scene.objects.from_id(terrain_info[terrain_key]["id"]))
            
        except:
            if not own_is_physics:
                logic.LibLoad("//" + global_dict["terrain_base_dir"] + terrain_name + ".blend", "Scene")
                
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

            global_dict[terrain_list_name][terrain_name][terrain_key] = {"players": [own_id], "id": terrain_id}
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
    check_near_terrains(own, own_id, own_pos, False, common.TERRAIN_IMAGE_MAX_DISTANCE)
    check_near_terrains(own, own_id, own_pos, True, common.TERRAIN_PHYSICS_MAX_DISTANCE)
