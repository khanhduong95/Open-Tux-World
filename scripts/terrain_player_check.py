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
    # own_id = id(own)
    own_name = own["terrain_name"]
    own_is_physics = own["physics"]
    if own_is_physics:
        min_dist = common.TERRAIN_PHYSICS_MAX_DISTANCE
        max_neighbors = common.TERRAIN_PHYSICS_MAX_NEIGHBORS
    else:
        min_dist = common.TERRAIN_IMAGE_MAX_DISTANCE
        max_neighbors = common.TERRAIN_IMAGE_MAX_NEIGHBORS

    own_pos = own.worldPosition
    
    x = int(own_pos[0] / min_dist)
    y = int(own_pos[1] / min_dist)

    if own_is_physics:
        z = int(own_pos[2] / min_dist)
        for key_x in range(x - max_neighbors, x + max_neighbors + 1):
            for key_y in range(y - max_neighbors, y + max_neighbors + 1):
                for key_z in range(z - max_neighbors, z + max_neighbors + 1):
                    key = str(key_x) + "_" + str(key_y) + "_" + str(key_z)
                    try:
                        if len(global_dict["terrain_physics_player_list"][key]) > 0:
                            return
                    except:
                        continue
    else:
        for key_x in range(x - max_neighbors, x + max_neighbors + 1):
            for key_y in range(y - max_neighbors, y + max_neighbors + 1):
                key = str(key_x) + "_" + str(key_y)
                try:
                    if len(global_dict["terrain_image_player_list"][key]) > 0:
                        return
                except:
                    continue

    terrain_lib = logic.expandPath("//" + global_dict["terrain_base_dir"] + own_name + ".blend")
    logic.LibFree(terrain_lib)
    print("terrain_player_check.py Terrain library " + terrain_lib + " freed")
    if own_is_physics:
        key = str(x) + "_" + str(y) + "_" + str(z)
        global_dict["terrain_physics_dict"].pop(key, None)
    else:
        key = str(x) + "_" + str(y)
        global_dict["terrain_image_dict"].discard(key)
        
    global_dict["active_terrain_list"].discard(own_name)
    own.endObject()
    print("terrain_player_check.py Terrain " + own_name + " removed")
