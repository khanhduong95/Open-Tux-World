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
from bge import logic

def main(cont):
    own = cont.owner
    try:
        dist_loc = own.getDistanceTo(logic.getCurrentScene().objects["player_loc"]) #distance to player_loc
        dist_cam = own.getDistanceTo(logic.getCurrentScene().objects["cam_pos"]) #distance to camera
        if own["death"]:
            if dist_loc >= 240 or (dist_loc > 40 and dist_loc - dist_cam > 0):
                own.endObject()
        else:
            if dist_loc >= 270 or (dist_loc > 100 and dist_loc - dist_cam > 0):
                own.endObject()
    except:
        pass#own.endObject()
