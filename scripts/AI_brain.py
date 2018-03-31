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
import math

logic = common.logic
scene = logic.getCurrentScene()

def attacked_action(cont, own, armature, front_sensor, front_lower_sensor, attacker, attacker_dist, attacker_vec):
    own["item"] = item = switch_item.check_item_previous(own, 2)
    weapons = set([1, 2])
    aim = (attacker_dist < 5 if item not in weapons else attacker_dist < 15) if own.children["AI_shoot_point"].children["AI_shoot_check"]["clear"] else False
    if aim:
        own.alignAxisToVect([attacker_vec.x, attacker_vec.y, 0], 0, 0.3)
        front_sensor.worldOrientation = front_lower_sensor.worldOrientation = own.worldOrientation
        own["hit"] = attacker_dist < 3 if item not in weapons else attacker_dist < 15

        if own["hit"]:

            if item in weapons and attacker_dist > 10:
                own["moving"] = forward = True
            else:
                forward = False
                
        else:
            own["moving"] = forward = True
    else:
        own["moving"] = forward = True
        
    own.children["AI_shoot_point"]["aim"] = armature["aim"] = aim
    armature["forward"] = forward
    armature["back"] = back = False
    armature["left"] = left = False
    armature["right"] = right = False

    AI_motion.main(cont, own, forward, back, left, right, aim)
    return aim
        
def attacked_move(cont, own, brain, armature, left_right, sensor_dir, front_sensor, front_lower_sensor, attacker, attacker_dist, attacker_vec):

    align_vect = [-attacker_vec.x, -attacker_vec.y, 0] if brain == 0 else [attacker_vec.x, attacker_vec.y, 0]
    front_sensor.alignAxisToVect(align_vect, 0, 1)
    front_lower_sensor.alignAxisToVect(align_vect, 0, 1)

    front_sensor["left_right"] = left_right
    armature["forward"] = forward = True
    armature["back"] = back = False
    armature["left"] = left = False
    armature["right"] = right = False
    own.children["AI_shoot_point"]["aim"] = armature["aim"] = aim = False
    AI_motion.main(cont, own, forward, back, left, right, aim)

def main(cont):
    own = cont.owner
    armature = own.children["AI_Armature"]
    fall = own["fall"] = not own.children["AI_lower_sensor"]["collision"]
    brain = own["brain"]
    if fall:
        own.state = logic.KX_STATE3
    else:
        front_sensor = own.children["AI_front_sensor"]
        front_lower_sensor = own.children["AI_front_lower_sensor"]
        left_right = front_sensor["left_right"]
        sensor_dir = front_sensor.children["AI_sensor_dir"]
        front_blocked = front_sensor["collision"] or not front_lower_sensor["collision"]
        if not own["normal"]:
            try:
                attacker = scene.objects.from_id(own["attacker_ID"])
                attacker_health = attacker["health"]
                if 'penguin' not in attacker:
                    print(attacker)
            except:
                own["run"] = own["aim"] = False
                own["item"] = 0
                own["normal"] = True
                return

            attacker_dist = own.getDistanceTo(attacker)
            if attacker_health < 1:
                own["run"] = own["aim"] = False
                own["item"] = 0
                own["normal"] = True
                return

            attacker_vec = own.worldPosition - attacker.worldPosition
            if brain != 0 and attacked_action(cont, own, armature, front_sensor, front_lower_sensor, attacker, attacker_dist, attacker_vec):
                return
            
        if front_blocked:
                
            if left_right == 0:
                armature["forward"] = forward = False
                left_right = randint(1, 2)

            else:
                rot_angle = math.radians(-45 if left_right == 1 else 45)
                front_sensor.applyRotation([0, 0, rot_angle], False)
                front_lower_sensor.applyRotation([0, 0, rot_angle], False)
                forward = armature["forward"]

            armature["back"] = back = False
            armature["left"] = left = False
            armature["right"] = right = False 
            armature["aim"] = aim = False
            AI_motion.main(cont, own, forward, back, left, right, aim)
            front_sensor["left_right"] = left_right

        else:
            sensor_vec = own.worldPosition - sensor_dir.worldPosition
            own.alignAxisToVect([sensor_vec.x, sensor_vec.y, 0], 0, 0.3)
            if own["normal"]:
                if brain == 2:
                    AI_list = logic.globalDict["AI_list"]
                    if AI_list:
                        attacker_ID = choice(AI_list) #find someone to attack
                        if attacker_ID != id(own):
                            own["attacker_ID"] = attacker_ID
                            own["normal"] = False
                            return
                        
                front_sensor.worldOrientation = front_lower_sensor.worldOrientation = own.worldOrientation
                armature["forward"] = forward = True
                armature["back"] = back = False
                armature["left"] = left = False
                armature["right"] = right = False
                armature["aim"] = aim = False
                AI_motion.main(cont, own, forward, back, left, right, aim)
                left_right = 0
                front_sensor["left_right"] = left_right

            else:
                own["run"] = True
                attacked_move(cont, own, brain, armature, left_right, sensor_dir, front_sensor, front_lower_sensor, attacker, attacker_dist, attacker_vec)
