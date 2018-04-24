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

def main(cont):
    own = cont.owner
    own_id = id(own)
    own_name = own["terrain_name"]
    own_is_physics = own["physics"]
    if own_is_physics:
        physics_or_image = "physics"
        min_dist = common.TERRAIN_PHYSICS_MAX_DISTANCE
        max_neighbors = common.TERRAIN_PHYSICS_MAX_NEIGHBORS
    else:
        physics_or_image = "image"
        min_dist = common.TERRAIN_IMAGE_MAX_DISTANCE
        max_neighbors = common.TERRAIN_IMAGE_MAX_NEIGHBORS

    terrain_list_name = "terrain_" + physics_or_image + "_list"
    own_pos = own.worldPosition
    
    x = int(own_pos[0] / min_dist)
    y = int(own_pos[1] / min_dist)

    if own_is_physics:
        z = int(own_pos[2] / min_dist)
        
    for player_id in global_dict[terrain_list_name][own_name]["players"]:
        try:
            player = scene.objects.from_id(player_id)
            player_pos = player.worldPosition
            player_x = int(player_pos[0] / min_dist)
            if player_x <= x + max_neighbors and player_x >= x - max_neighbors:
                player_y = int(player_pos[1] / min_dist)
                if player_y <= y + max_neighbors and player_y >= y - max_neighbors:
                    if own_is_physics:
                        player_z = int(player_pos[2] / min_dist)
                        if player_z <= z + max_neighbors and player_z >= z - max_neighbors:
                            continue
                    else:
                        continue
        except:
            raise
            
        global_dict[terrain_list_name][own_name]["players"].remove(player_id)

    if not global_dict[terrain_list_name][own_name]["players"]:
        del global_dict[terrain_list_name][own_name]
        own.endObject()
        if not own_is_physics:
            terrain_lib = logic.expandPath("//" + global_dict["terrain_base_dir"] + own_name + ".blend")
            logic.LibFree(terrain_lib)
            global_dict["terrain_dict"].pop(str(x) + "_" + str(y), None)
            print("Terrain library " + terrain_lib + " removed")
        print("Terrain " + physics_or_image + " " + own_name + " " + str(own_id) + " removed")
