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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from scripts import common

=======
>>>>>>> 99a89667972cec7d9a2bfa8a3e814e7544eac66b
=======
>>>>>>> parent of fd4461f... add steep move
=======
>>>>>>> parent of fd4461f... add steep move
def turn(own, run, left, right):
    speed = 0.02 if run else 0.01
    own.applyRotation([0, 0, speed if left else (-speed if right else 0)], True)

def main(cont, own, forward, back, left, right, aim):
    run = own["run"]
    own.worldOrientation[2] = [0.0, 0.0, 1.0]
    if aim:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (left or right) != (forward or back):
            speed = 10
        else:
            speed = 7 if (left or right) and (forward or back) else 0

        v_x = -speed if forward else (speed if back else 0)
        v_y = -speed if left else (speed if right else 0)
        v_z = common.steep_speed(own, own.children["AI_steep_dir"], aim, speed, forward, back, left, right)
        own.setLinearVelocity([v_x, v_y, v_z], True)
            
    else:
        if forward:
            v_x = -20 if run else -10
            own.setLinearVelocity([v_x, 0, common.steep_speed(own, own.children["AI_steep_dir"], False, -v_x, forward, back, left, right)], True)
=======
        speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
        own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
            
    else:
        if forward:
            own.setLinearVelocity([-20 if run else -10, 0, 0], True)
>>>>>>> 99a89667972cec7d9a2bfa8a3e814e7544eac66b
=======
        speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
        own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
            
    else:
        if forward:
            own.setLinearVelocity([-20 if run else -10, 0, 0], True)
>>>>>>> parent of fd4461f... add steep move
=======
        speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
        own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
            
    else:
        if forward:
            own.setLinearVelocity([-20 if run else -10, 0, 0], True)
>>>>>>> parent of fd4461f... add steep move
            if left or right:
                turn(own, run, left, right)

        else:
            if own["moving"]:
                own.setLinearVelocity([0.00000012, 0, 0], True)
                own["moving"] = False
            elif left or right:
                turn(own, run, left, right)
