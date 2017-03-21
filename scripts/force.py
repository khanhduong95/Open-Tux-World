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
scene = common.scene

def border_check(own):
    if own.worldPosition[0] < -common.TERRAIN_BORDER_X:
        own.worldPosition[0] = -common.TERRAIN_BORDER_X
    elif own.worldPosition[0] > common.TERRAIN_BORDER_X:
        own.worldPosition[0] = common.TERRAIN_BORDER_X
    if own.worldPosition[1] < -common.TERRAIN_BORDER_Y:
        own.worldPosition[1] = -common.TERRAIN_BORDER_Y
    elif own.worldPosition[0] > common.TERRAIN_BORDER_Y:
        own.worldPosition[1] = common.TERRAIN_BORDER_Y
    if own.worldPosition[2] <= 0:
        own.worldPosition = scene.objects["terrain_spawner"].worldPosition
        if own.worldPosition[2] <= 0:
            own.worldPosition[2] += 5

def main(cont):
    own = cont.owner
    border_check(own)

    v = Vector((own["v_x"],own["v_y"],own["v_z"]))
    dv = Vector(own.worldLinearVelocity) - v
    v += dv
    speed = common.getDistance([dv.x, dv.y, dv.z])
    if speed > common.DANGER_SPEED:
        if speed > common.FATAL_SPEED:
            own["health"] = 0
        elif speed > common.HIGH_DANGER_SPEED:
            own["health"] -= speed * common.HIGH_DAMAGE_RATE
        else:
            own["health"] -= speed * common.DAMAGE_RATE
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
