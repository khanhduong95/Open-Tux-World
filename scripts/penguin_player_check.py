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
    parent = own.parent
    
    if "player" in parent and parent["health"] > 0:
        return
    
    own_id = id(own)
    parent_id = id(parent)
    
    for player_id in global_dict["player_list"]:
        try:
            player = scene.objects.from_id(player_id).groupObject
            dist_loc = own.getDistanceTo(player.groupMembers["player_loc"]) #distance to player_loc
            dist_cam = own.getDistanceTo(player.groupMembers["cam_pos"]) #distance to camera

            far_death = parent["health"] < 1 and (dist_loc > common.AI_DIST_LOC_MAX_DEATH or (dist_loc > common.AI_DIST_LOC_MIN_DEATH and dist_loc > dist_cam))
            far_alive = dist_loc > common.AI_DIST_LOC_MAX or (dist_loc > common.AI_DIST_LOC_MIN and dist_loc > dist_cam)
            if not far_death and not far_alive:
                return
            
        except:
            continue

    if "AI" in own:
        global_dict["AI_list"].remove(parent_id)

    parent.endObject()
    own.groupObject.endObject()
    print("AI " + str(parent_id) + " removed")
