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
import scripts.common_functions as cf
from mathutils import Vector

DANGER_SPEED = 40
HIGH_DANGER_SPEED = 60
FATAL_SPEED = 80
DAMAGE_RATE = 0.05
HIGH_DAMAGE_RATE = 0.15

logic = cf.logic

def main(cont):
    own = cont.owner
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    speed = cf.getDistance([dv.x, dv.y, dv.z])
    if speed > DANGER_SPEED:
        if speed > FATAL_SPEED:
            own["health"] = 0
        elif speed > HIGH_DANGER_SPEED:
            own["health"] -= speed * HIGH_DAMAGE_RATE
        else:
            own["health"] -= speed * DAMAGE_RATE
        #print(own)
        #print(own["health"])
        own.state = logic.KX_STATE3

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own["hit_released"] = False
        own["death"] = True
        own.state = logic.KX_STATE4
