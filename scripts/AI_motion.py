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
def turn(own, run, left, right):
    speed = 0.02 if run else 0.01
    own.applyRotation([0, 0, speed if left else (-speed if right else 0)], True)

def main(cont, own, forward, back, left, right, aim):
    run = own["run"]
    own.worldOrientation[2] = [0.0, 0.0, 1.0]
    if aim:
        speed = 10 if (left or right) != (forward or back) else (7 if (left or right) and (forward or back) else 0)
        own.setLinearVelocity([-speed if forward else (speed if back else 0), -speed if left else (speed if right else 0), 0], True)
            
    else:
        if forward:
            own.setLinearVelocity([-20 if run else -10, 0, 0], True)
            if left or right:
                turn(own, run, left, right)

        else:
            if own["moving"]:
                own.setLinearVelocity([0.00000012, 0, 0], True)
                own["moving"] = False
            elif left or right:
                turn(own, run, left, right)
