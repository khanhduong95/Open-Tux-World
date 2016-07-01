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
import math
from mathutils import Vector

def main(cont):
    own = cont.owner
    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    max_dv = max(dv.x,dv.y,dv.z)
    min_dv = min(dv.x,dv.y,dv.z)
    if max_dv > 40:
        if max_dv > 60:
            own["health"] -= max_dv * 0.1
        else:
            own["health"] -= max_dv * 0.05
        print(own)
        print(own["health"])
        own.state = logic.KX_STATE3

    elif min_dv < -40:
        if min_dv < -60:
            own["health"] -= -min_dv * 0.1
        else:
            own["health"] -= -min_dv * 0.05
        print(own)
        print(own["health"])
        own.state = logic.KX_STATE3

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own["hit_released"] = False
        own["death"] = True
        own.state = logic.KX_STATE4
