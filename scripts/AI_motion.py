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

def turn_fast(run):
    if run:
        return 0.02
    else:
        return 0.01

def turn_left_right(left, right, speed):
    if left:
        return speed
    elif right:
        return -speed
    else:
        return 0
    
def turn(own, run, left, right):
    speed = turn_fast(run)
    own.applyRotation([0, 0, turn_left_right(left, right, speed)], True)
    
def aim_move_left_right(left, right, speed):
    if left:
        return -speed
    elif right:
        return speed
    else:
        return 0
    
def aim_move_forward_back(forward, back, speed):
    if forward:
        return -speed
    elif back:
        return speed
    else:
        return 0
    
def aim_move_straight(straight):
    if straight:
        return 10
    else:
        return 7
    
def aim_move(own, forward, back, left, right):

    if left or right:
        speed = aim_move_straight(not (forward or back))
        own.setLinearVelocity([aim_move_forward_back(forward, back, speed), aim_move_left_right(left, right, speed), 0], True)

    elif forward or back:
        own.setLinearVelocity([aim_move_forward_back(forward, back, aim_move_straight(True)), 0, 0], True)

def move_fast(run):
    if run:
        return -20
    else:
        return -10
        
def move(own, run):
    own.setLinearVelocity([move_fast(run), 0, 0], True)

def stop(own):
    own.setLinearVelocity([0.00000012, 0, 0], True)
    own["moving"] = False
    own.setLinearVelocity([0, 0, 0], True)

def main(cont, own, forward, back, left, right, aim):
    run = own["run"]
    own.worldOrientation[2] = [0.0, 0.0, 1.0]
    if aim:
        aim_move(own, forward, back, left, right)
    else:
        if forward:
            move(own, run)
            if left or right:
                turn(own, run, left, right)

        else:
            if own["moving"]:
                stop(own)
            elif left or right:
                turn(own, run, left, right)
