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

def rigid_main(cont):
    if keyboard.events[events.RKEY] == JUST_ACTIVATED:
        cont.activate(cont.actuators["Message"])
        cont.activate(cont.actuators["Delete"])

def main(cont):
    own = cont.owner
    armature = own.children["Armature"]
    FALL = own["FALL"] = not own.children["lower_cube"]["collision"]
    FORWARD = armature["FORWARD"] = keyboard.events[events.WKEY] == ACTIVE
    LEFT = armature["LEFT"] = keyboard.events[events.AKEY] == ACTIVE
    BACK = armature["BACK"] = keyboard.events[events.SKEY] == ACTIVE
    RIGHT = armature["RIGHT"] = keyboard.events[events.DKEY] == ACTIVE
    JUMP = keyboard.events[events.SPACEKEY] == ACTIVE
    own["RUN"] = keyboard.events[events.LEFTSHIFTKEY] == ACTIVE or keyboard.events[events.RIGHTSHIFTKEY] == ACTIVE
    AIM = own.children["shoot_point"]["AIM"] = armature["AIM"] = mouse.events[events.RIGHTMOUSE] == ACTIVE
    own["HIT"] = mouse.events[events.LEFTMOUSE] == JUST_ACTIVATED
    previous_item = keyboard.events[events.QKEY] == JUST_ACTIVATED or mouse.events[events.WHEELDOWNMOUSE] == JUST_ACTIVATED
    next_item = mouse.events[events.WHEELUPMOUSE] == JUST_ACTIVATED
    switch_item.main(own, previous_item, next_item)
    eat.main(own, keyboard.events[events.EKEY] == JUST_ACTIVATED, own["item"], own["fish"], own["health"], 90)
    player_motion.main(cont, own, FORWARD, BACK, LEFT, RIGHT, JUMP, AIM, FALL)
