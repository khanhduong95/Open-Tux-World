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
from scripts import common, AI_motion, switch_item, eat
from random import randint, choice

logic = common.logic
scene = logic.getCurrentScene()

def attacked_state(cont, own, brain, armature, front_sensor, attacker):
    left_right = own["left_right"]
    vec = own.worldPosition - attacker.worldPosition
    if brain == 0:
        if front_sensor:
            forward = False
            if left_right == 0:
                left_right = randint(1, 2)

            left = left_right == 1
            right = left_right == 2
        else:
            if left_right == 0:
                own.alignAxisToVect([-vec.x , -vec.y, 0], 0, 0.5)#point away from attacker
                left = right = False
            else:
                left = left_right == 1
                right = left_right == 2
                left_right = 0

            forward = own["moving"] = True
        aim = False
        back = False

    else:
        distance = own.getDistanceTo(attacker)
        own["item"] = switch_item.check_item_previous(own, 2)
        if front_sensor and distance > 2:
            aim = False
            forward = False
            if left_right == 0:
                left_right = randint(1,2)

            left = left_right == 1
            right = left_right == 2
        else:
            own.alignAxisToVect([vec.x , vec.y, 0], 0, 0.5)#point to attacker
            if distance < 5 or (distance < 15 and own["item"] != 0):
                aim = True
                if own["item"] == 0:
                    own["hit"] = distance < 2# and not 10 < armature["upper_current_frame"] <= 30
                else:
                    own["hit"] = distance < 15# and not 10 < armature["upper_current_frame"] <= 30
                if own["hit"]:
                    forward = False
                else:
                    forward = own["moving"] = True
            else:
                aim = False
                forward = own["moving"] = True

            if left_right != 0:
                left_right = 0
            left = right = False
        back = False

    own["left_right"] = left_right
    armature["forward"] = forward
    armature["back"] = back
    armature["left"] = left
    armature["right"] = right
    own.children["AI_shoot_point"]["aim"] = armature["aim"] = aim
    AI_motion.main(cont, own, forward, back, left, right, aim)

def normal_state(cont, own, brain, armature, front_sensor):
    left_right = own["left_right"]

    if own["item"] != 0:
        own["item"] = 0

    if front_sensor:
        forward = False
        if left_right == 0:
            left_right = randint(1, 2)

        left = left_right == 1
        right = left_right == 2
    else:
        forward = own["moving"] = True
        if left_right != 0:
            left_right = 0

        left = right = False

    own["left_right"] = left_right
    armature["forward"] = forward
    armature["back"] = back = False
    armature["left"] = left
    armature["right"] = right
    AI_motion.main(cont, own, forward, back, left, right, False)

def main(cont):
    own = cont.owner
    armature = own.children["AI_Armature"]
    fall = own["fall"] = not own.children["AI_lower_sensor"]["collision"]
    brain = own["brain"]
    if fall:
        own.state = logic.KX_STATE3
    else:
        front_sensor = own.children["AI_front_sensor"]["collision"]
        if own["normal"]:
            if own["brain"] == 2:
                AI_list = logic.globalDict["AI_list"]
                if AI_list:
                    attacker_ID = choice(AI_list) #find someone to attack
                    if attacker_ID != id(own):
                        own["attacker_ID"] = attacker_ID
                        own["normal"] = False
                        return
            armature["aim"] = own["run"] = False
            normal_state(cont, own, brain, armature, front_sensor)
        else:
            try:
                attacker = scene.objects.from_id(own["attacker_ID"])
                if own.getDistanceTo(attacker) >= 150 or attacker["death"]:
                    own["normal"] = True
                else:
                    own["run"] = True
                    attacked_state(cont, own, brain, armature, front_sensor, attacker)
            except:
                own["normal"] = True
