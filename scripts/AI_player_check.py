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
    
    for player_id in logic.globalDict["player_list"]:
        try:
            player = scene.objects.from_id(player_id)
            dist_loc = own.getDistanceTo(player.children["player_loc"]) #distance to player_loc
            dist_cam = own.getDistanceTo(player.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"]) #distance to camera

            far_death = parent["health"] < 1 and (dist_loc > common.AI_DIST_LOC_MAX_DEATH or (dist_loc > common.AI_DIST_LOC_MIN_DEATH and dist_loc > dist_cam))
            far_alive = dist_loc > common.AI_DIST_LOC_MAX or (dist_loc > common.AI_DIST_LOC_MIN and dist_loc > dist_cam)
            if not far_death and not far_alive:
                return
            
        except:
            continue

    logic.globalDict["AI_list"].remove(id(parent))
    parent.endObject()
