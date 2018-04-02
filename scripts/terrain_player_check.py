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
    physics_or_image = "physics" if own_is_physics else "image"
    min_dist = common.TERRAIN_PHYSICS_MAX_DISTANCE if own_is_physics else common.TERRAIN_IMAGE_MAX_DISTANCE
    own_pos = own.worldPosition
    terrain_list_name = "terrain_" + physics_or_image + "_list"
    
    x = str(own_pos[0] // min_dist)
    y = str(own_pos[1] // min_dist)
    key = x+"_"+y

    if own_is_physics:
        z = str(own_pos[2] // min_dist)
        key += "_"+z
        
    for player_id in global_dict[terrain_list_name][own_name][key]["players"]:
        try:
            player = scene.objects.from_id(player_id)
            player_pos = player.worldPosition
            player_x = str(player_pos[0] // min_dist)
            player_y = str(player_pos[1] // min_dist)
            player_key = player_x + "_" + player_y
            
            if own_is_physics:
                player_z = str(player_pos[2] // min_dist)
                player_key += "_" + player_z

            if global_dict["terrain_dict"][physics_or_image][player_key]["location"] != own.worldPosition:
                global_dict[terrain_list_name][own_name][key]["players"].remove(player_id)
        except:
            continue

    if not global_dict[terrain_list_name][own_name][key]["players"]:
        del global_dict[terrain_list_name][own_name][key]
        own.endObject()
        print("Terrain " + physics_or_image + " " + own_name + " " + str(own_id) + " removed")
