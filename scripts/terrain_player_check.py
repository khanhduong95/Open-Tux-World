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

def main(cont):
    own = cont.owner
    parent = own.parent
    parent_id = id(parent)
    parent_name = parent.name
    physics_or_image = "physics" if parent_name.endswith("_physics_group") else "images"
    min_dist = 100 if physics_or_image == "physics" else 500
    own_pos = own.worldPosition
    terrain_list_name = "terrain_" + physics_or_image + "_list"
    
    x = str(own_pos[0] // min_dist)
    y = str(own_pos[1] // min_dist)
    key = x+"_"+y

    if physics_or_image == "physics":
        z = str(own_pos[2] // min_dist)
        key += "_"+z
        
    global_dict = logic.globalDict
    # if key not in global_dict[terrain_list_name][parent_name]:
    #     print("STOP " + parent_name +" key "+key)        
    #     print(global_dict[terrain_list_name][parent_name])
    #     return
    # if "players" not in global_dict[terrain_list_name][parent_name][key]:
    #     print("STOP players")
    #     print(global_dict[terrain_list_name][parent_name][key])
    #     return
    for player_id in global_dict[terrain_list_name][parent_name][key]["players"]:
        try:
            player = scene.objects.from_id(player_id)
            player_pos = player.worldPosition
            player_x = str(player_pos[0] // min_dist)
            player_y = str(player_pos[1] // min_dist)
            player_key = player_x + "_" + player_y
            
            if physics_or_image == "physics":
                player_z = str(player_pos[2] // min_dist)
                player_key += "_" + player_z

            if global_dict["terrains_dict"][physics_or_image][player_key]["location"] != parent.worldPosition:
                global_dict[terrain_list_name][parent_name][key]["players"].remove(player_id)
        except:
            continue

    if not global_dict[terrain_list_name][parent_name][key]["players"]:
        del global_dict[terrain_list_name][parent_name][key]
        print("Terrain " + physics_or_image + " " + parent_name + " " + str(parent_id) + " removed")
        parent.endObject()
