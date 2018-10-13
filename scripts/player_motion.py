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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from scripts import common

def aim_move(own, forward, back, left, right):
    if (left or right) != (forward or back):
        speed = 10
    else:
        speed = 7 if (left or right) and (forward or back) else 0

    v_x = -speed if forward else (speed if back else 0)
    v_y = -speed if left else (speed if right else 0)
    v_z = common.steep_speed(own, own.children["steep_dir"], True, speed, forward, back, left, right)
    own.setLinearVelocity([v_x, v_y, v_z], True)
=======

def aim_move(own, forward, back, left, right):
    speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
    own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
>>>>>>> 99a89667972cec7d9a2bfa8a3e814e7544eac66b
=======

def aim_move(own, forward, back, left, right):
    speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
    own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
>>>>>>> parent of fd4461f... add steep move
=======

def aim_move(own, forward, back, left, right):
    speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
    own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
>>>>>>> parent of fd4461f... add steep move
=======

def aim_move(own, forward, back, left, right):
    speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
    own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
>>>>>>> parent of fd4461f... add steep move
    
def move(cont, forward_dir, forward, back, left, right, run, run_fast, jump):
    cont.activate(cont.actuators["forward_dir"])
    own = cont.owner
    forward_dir.localPosition[0] = -3 if forward else (3 if back else 0)
    forward_dir.localPosition[1] = -3 if left else (3 if right else 0)
        
    cont.activate(cont.actuators["Mouse"])
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    v_x = -30 if run_fast else (-20 if run else -10)
    v_z = 6 if jump else common.steep_speed(own, own.children["steep_dir"], False, -v_x, forward, back, left, right)
    own.setLinearVelocity([v_x, 0, v_z], True)
=======
    own.setLinearVelocity([-30 if run_fast else (-20 if run else -10), 0, 6 if jump else 0], True)
>>>>>>> 99a89667972cec7d9a2bfa8a3e814e7544eac66b
=======
    own.setLinearVelocity([-30 if run_fast else (-20 if run else -10), 0, 6 if jump else 0], True)
>>>>>>> parent of fd4461f... add steep move
=======
    own.setLinearVelocity([-30 if run_fast else (-20 if run else -10), 0, 6 if jump else 0], True)
>>>>>>> parent of fd4461f... add steep move
=======
    own.setLinearVelocity([-30 if run_fast else (-20 if run else -10), 0, 6 if jump else 0], True)
>>>>>>> parent of fd4461f... add steep move

def main(cont, own, forward, back, left, right, jump, aim, fall):
    forward_dir = own.children["camera_track"].children["forward_dir"]
    cont.deactivate(cont.actuators["Mouse"])
    cont.deactivate(cont.actuators["forward_dir"])
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
            own.setLinearVelocity([0.00000012, 0, 0])
            own["moving"] = False
