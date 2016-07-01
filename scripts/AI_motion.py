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
def turn_left(own, RUN):
    if RUN:
        own.applyRotation([0,0,0.02],True)
    else:
        own.applyRotation([0,0,0.01],True)

def turn_right(own, RUN):
    if RUN:
        own.applyRotation([0,0,-0.02],True)
    else:
        own.applyRotation([0,0,-0.01],True)

def aim_move(own, FORWARD, BACK, LEFT, RIGHT):

    if LEFT:
        if FORWARD:
            own.setLinearVelocity([-7,-7,0],True)

        elif BACK:
            own.setLinearVelocity([7,-7,0],True)

        else:
            own.setLinearVelocity([0,-10,0],True)

    elif RIGHT:
        if FORWARD:
            own.setLinearVelocity([-7,7,0],True)

        elif BACK:
            own.setLinearVelocity([7,7,0],True)

        else:
            own.setLinearVelocity([0,10,0],True)

    elif FORWARD:
        own.setLinearVelocity([-10,0,0],True)

    elif BACK:
        own.setLinearVelocity([10,0,0],True)


def move(own, RUN):
    if RUN:
        own.setLinearVelocity([-20,0,0], True)
    else:
        own.setLinearVelocity([-10,0,0], True)

def stop(own):
    own.setLinearVelocity([0.00000012,0,0])
    own["moving"] = False
    own.setLinearVelocity([0,0,0])

def main(cont, own, FORWARD, BACK, LEFT, RIGHT, AIM):
    RUN = own["RUN"]
    if own.worldOrientation[2] != [0.0,0.0,1.0]:
        own.worldOrientation[2] = [0.0,0.0,1.0]
    if AIM:
        aim_move(own, FORWARD, BACK, LEFT, RIGHT)
    else:
        if FORWARD:
            move(own, RUN)
            if LEFT:
                turn_left(own, RUN)
            elif RIGHT:
                turn_right(own, RUN)
        else:
            if own["moving"]:
                stop(own)
            elif LEFT:
                turn_left(own, RUN)
            elif RIGHT:
                turn_right(own, RUN)

