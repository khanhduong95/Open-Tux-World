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

DIST_LOC_MAX = 270
DIST_LOC_MIN = 100

DIST_LOC_MAX_DEATH = 240
DIST_LOC_MIN_DEATH = 40

DIST_LOC_CAM = 0
DIST_LOC_CAM_DEATH = 0

scene = logic.getCurrentScene()

def main(cont):
    own = cont.owner
    try:
        dist_loc = own.getDistanceTo(scene.objects["player_loc"]) #distance to player_loc
        dist_cam = own.getDistanceTo(scene.objects["cam_pos"]) #distance to camera
        if own["death"]:
            if dist_loc >= DIST_LOC_MAX_DEATH or (dist_loc > DIST_LOC_MIN_DEATH and dist_loc - dist_cam > DIST_LOC_CAM_DEATH):
                own.endObject()
        else:
            if dist_loc >= DIST_LOC_MAX or (dist_loc > DIST_LOC_MIN and dist_loc - dist_cam > DIST_LOC_CAM):
                own.endObject()
    except:
        pass
