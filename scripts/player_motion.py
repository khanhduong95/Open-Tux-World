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

def aim_move(own, forward, back, left, right):

    if left:
        if forward:
            own.setLinearVelocity([-7, -7, 0], True)

        elif back:
            own.setLinearVelocity([7, -7, 0], True)

        else:
            own.setLinearVelocity([0, -10, 0], True)

    elif right:
        if forward:
            own.setLinearVelocity([-7, 7, 0], True)

        elif back:
            own.setLinearVelocity([7, 7, 0], True)

        else:
            own.setLinearVelocity([0, 10, 0], True)

    elif forward:
        own.setLinearVelocity([-10, 0, 0], True)

    elif back:
        own.setLinearVelocity([10, 0, 0], True)

def normal_move(own, run, run_fast, jump):
    if run_fast:
        if jump:
            own.setLinearVelocity([-30, 0, 6], True)
        else:
            own.setLinearVelocity([-30, 0, 0], True)
    elif run:
        if jump:
            own.setLinearVelocity([-20, 0, 6], True)
        else:
            own.setLinearVelocity([-20, 0, 0], True)
    else:
        if jump:
            own.setLinearVelocity([-10, 0, 6], True)
        else:
            own.setLinearVelocity([-10, 0, 0], True)

def stop(own):
    own.setLinearVelocity([0.00000012, 0, 0])
    own["moving"] = False
    own.setLinearVelocity([0, 0, 0])

def act_actuator(cont, name):
    cont.activate(cont.actuators[name])
    
def deact_actuator(cont, name):
    cont.deactivate(cont.actuators[name])
    
def move(cont, forward_dir, forward, back, left, right, run, run_fast, jump):
    act_actuator(cont, "forward_dir")
    own = cont.owner
    if forward:
        forward_dir.localPosition[0] = -3
    elif back:
        forward_dir.localPosition[0] = 3
    else:
        forward_dir.localPosition[0] = 0
        
    if left:
        forward_dir.localPosition[1] = -3
    elif right:
        forward_dir.localPosition[1] = 3
    else:
        forward_dir.localPosition[1] = 0

    act_actuator(cont, "Mouse")
    normal_move(own, run, run_fast, jump)

def main(cont, own, forward, back, left, right, jump, aim, fall):
    forward_dir = own.children["camera_track"].children["forward_dir"]
    deact_actuator(cont, "Mouse")
    deact_actuator(cont, "forward_dir")
    forward_dir.localPosition[0] = -3
    forward_dir.localPosition[1] = 0

    own.worldOrientation[2] = [0.0, 0.0, 1.0]
    sun_moon = logic.getCurrentScene().objects["sun_moon_holder_parent"]
    sun_moon.worldPosition.x = own.worldPosition.x
    sun_moon.worldPosition.y = own.worldPosition.y

    if fall:
        own.state = logic.KX_STATE3
    else:
        run = own["run"]
        run_fast = own.children["Armature"]["run_fast"] = run and own["stamina"] > 0
        if forward or back or left or right:
            own["moving"] = True
            if aim:
                aim_move(own, forward, back, left, right)

            else:
                move(cont, forward_dir, forward, back, left, right, run, run_fast, jump)

        elif jump:
            own.setLinearVelocity([0, 0, 6], True)

        elif own["moving"]:
            stop(own)
