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
from mathutils import Vector

logic = common.logic

def gravity(cont):
    own = cont.owner
    
    own.applyForce([0, 0, -10 * own.mass], False)
    # v = own["v_z"]
    # if v > 0:
    #     v = 0
    #     own.applyForce([0, 0, -100], False)
    # elif v >= -150:
    #     v -= 0.5
    #     own.applyForce([0, 0, 100 * v], False)
    # own["v_z"] = v

def main(cont):
    own = cont.owner
    own["hit"] = False
    own.enableRigidBody()
    v = Vector((own["v_x"], own["v_y"], own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    speed = common.getDistance([dv.x, dv.y, dv.z])
    if speed > common.DANGER_SPEED:
        if speed > common.FATAL_SPEED:
            own["health"] = 0
        else:
            own["health"] -= speed * (common.HIGH_DAMAGE_RATE if speed > common.HIGH_DANGER_SPEED else common.DAMAGE_RATE)
        own.state = logic.KX_STATE3

    own["v_x"] = v.x
    own["v_y"] = v.y
    own["v_z"] = v.z

    if own["health"] <= 0:
        own["hit_released"] = False
        own["death"] = True
        own.state = logic.KX_STATE4
    elif speed > common.RIGID_SPEED and (cont.sensors["Collision.001"].positive or not own["fall"]):
        own.disableRigidBody()
        own.worldOrientation[2] = [0.0,0.0,1.0]
        own.state = logic.KX_STATE2
