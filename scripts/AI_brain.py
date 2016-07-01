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
from scripts import AI_motion, switch_item
from random import randint

def attacked_state(cont, own, brain, armature, front_sensor, attacker):
    left_right = own["left_right"]

    if brain == 0:
        if front_sensor:
            FORWARD = False
            if left_right == 0:
                left_right = randint(1,2)

            LEFT = left_right == 1
            RIGHT = left_right == 2
        else:
            if left_right == 0:
                flee = cont.actuators["flee"]
                flee.object = attacker
                cont.activate(flee)
                cont.deactivate(flee)
                LEFT = RIGHT = False
            else:
                print(left_right)
                LEFT = left_right == 1
                RIGHT = left_right == 2
                left_right = 0

            FORWARD = own["moving"] = True
        AIM = False
        BACK = False

    elif brain == 1:
        distance = own.getDistanceTo(attacker)
        own["item"] = switch_item.check_item_previous(own, 2)
        if front_sensor and distance > 2:
            AIM = False
            FORWARD = False
            if left_right == 0:
                left_right = randint(1,2)

            LEFT = left_right == 1
            RIGHT = left_right == 2
        else:
            find = cont.actuators["attacker_find"]
            find.object = attacker
            cont.activate(find)
            cont.deactivate(find)
            if distance < 5 or (distance < 15 and own["item"] != 0):
                AIM = True
                if own["item"] == 0:
                    own["HIT"] = (distance < 2 and not 10 < armature["upper_frame"] <= 30)
                else:
                    own["HIT"] = (distance < 15 and not 10 < armature["upper_frame"] <= 30)
                FORWARD = not own["HIT"]
            else:
                AIM = False
                FORWARD = True
            own["moving"] = True

            if left_right != 0:
                left_right = 0
            LEFT = RIGHT = False
        BACK = False

    own["left_right"] = left_right
    armature["FORWARD"] = FORWARD
    armature["BACK"] = BACK
    armature["LEFT"] = LEFT
    armature["RIGHT"] = RIGHT
    own.children["AI_shoot_point"]["AIM"] = armature["AIM"] = AIM
    AI_motion.main(cont, own, FORWARD, BACK, LEFT, RIGHT, AIM)

def normal_state(cont, own, brain, armature, front_sensor):
    left_right = own["left_right"]

    if own["item"] != 0:
        own["item"] = 0

    if front_sensor:
        FORWARD = False
        if left_right == 0:
            left_right = randint(1,2)

        LEFT = left_right == 1
        RIGHT = left_right == 2
    else:
        FORWARD = own["moving"] = True
        if left_right != 0:
            left_right = 0

        LEFT = RIGHT = False

    own["left_right"] = left_right
    armature["FORWARD"] = FORWARD
    armature["BACK"] = BACK = False
    armature["LEFT"] = LEFT
    armature["RIGHT"] = RIGHT
    armature["BACK"] = BACK
    AI_motion.main(cont, own, FORWARD, BACK, LEFT, RIGHT, False)

def main(cont):
    own = cont.owner
    armature = own.children["AI_Armature"]
    FALL = own["FALL"] = not own.children["AI_lower_sensor"]["collision"]
    brain = own["brain"]
    if FALL:
        own.state = logic.KX_STATE3
    else:
        front_sensor = own.children["AI_front_sensor"]["collision"]
        if own["normal"]:
            armature["AIM"] = own["RUN"] = False
            normal_state(cont, own, brain, armature, front_sensor)
        else:
            try:
                attacker = logic.getCurrentScene().objects.from_id(own["attacker_ID"])
                if own.getDistanceTo(attacker) >= 150 or attacker["death"]:
                    own["normal"] = True
                else:
                    own["RUN"] = True
                    attacked_state(cont, own, brain, armature, front_sensor, attacker)
            except:
                own["normal"] = True
