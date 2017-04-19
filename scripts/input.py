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
from bge import logic, events
from scripts import player_motion, switch_item, eat

keyboard = logic.keyboard
mouse = logic.mouse
JUST_ACTIVATED = logic.KX_INPUT_JUST_ACTIVATED
ACTIVE = logic.KX_INPUT_ACTIVE

def cam(cont):
    own = cont.owner
    if keyboard.events[events.PKEY] == JUST_ACTIVATED:
        if own["pause"]:
            cont.activate(cont.actuators["resume"])
            own["pause"] = False
        else:
            cont.activate(cont.actuators["pause"])
            own["pause"] = True

def death_main(cont):
    if keyboard.events[events.RKEY] == JUST_ACTIVATED:
        own = cont.owner
        own.state = logic.KX_STATE1
        armature = own.children["Armature"]
        armature.state = logic.KX_STATE1
        armature.children["grab_point"].state = logic.KX_STATE1
        #cont.activate(cont.actuators["Message"])
        #cont.activate(cont.actuators["Delete"])

def main(cont):
    own = cont.owner
    armature = own.children["Armature"]
    fall = own["fall"] = not own.children["lower_cube"]["collision"]
    forward = armature["forward"] = keyboard.events[events.WKEY] == ACTIVE
    left = armature["left"] = keyboard.events[events.AKEY] == ACTIVE
    back = armature["back"] = keyboard.events[events.SKEY] == ACTIVE
    right = armature["right"] = keyboard.events[events.DKEY] == ACTIVE
    JUMP = keyboard.events[events.SPACEKEY] == ACTIVE
    own["run"] = keyboard.events[events.LEFTSHIFTKEY] == ACTIVE or keyboard.events[events.RIGHTSHIFTKEY] == ACTIVE
    aim = own.children["shoot_point"]["aim"] = armature["aim"] = mouse.events[events.RIGHTMOUSE] == ACTIVE
    if mouse.events[events.LEFTMOUSE] == JUST_ACTIVATED:
        own["hit"] = True
    previous_item = keyboard.events[events.QKEY] == JUST_ACTIVATED or mouse.events[events.WHEELDOWNMOUSE] == JUST_ACTIVATED
    next_item = mouse.events[events.WHEELUPMOUSE] == JUST_ACTIVATED
    switch_item.main(own, previous_item, next_item)
    eat.main(own, keyboard.events[events.EKEY] == JUST_ACTIVATED, own["item"], own["fish"], own["health"], 90)
    player_motion.main(cont, own, forward, back, left, right, JUMP, aim, fall)
