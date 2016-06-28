from bge import logic
from scripts import AI_motion
from random import randint

def attacked_state(cont, own, brain, armature, front_sensor, attacker):
    if brain == 0:
        if front_sensor:
            armature["FORWARD"] = FORWARD = False
            if own["left_right"] == 0:
                own["left_right"] = randint(1,2)

            armature["LEFT"] = LEFT = own["left_right"] == 1
            armature["RIGHT"] = RIGHT = own["left_right"] == 2
        else:
            armature["FORWARD"] = FORWARD = own["moving"] = True
            if own["left_right"] != 0:
                own["left_right"] = 0

            armature["LEFT"] = armature["RIGHT"] = LEFT = RIGHT = False
        AIM = False

    elif brain == 1:
        distance = own.getDistanceTo(attacker)
        if front_sensor and distance > 2:
            AIM = False
            armature["FORWARD"] = FORWARD = False
            if own["left_right"] == 0:
                own["left_right"] = randint(1,2)

            armature["LEFT"] = LEFT = own["left_right"] == 1
            armature["RIGHT"] = RIGHT = own["left_right"] == 2
        else:
            find = cont.actuators["attacker_find"]
            find.object = attacker
            cont.activate(find)
            cont.deactivate(find)
            if distance < 5:
                AIM = True
                own["HIT"] = (distance < 2 and not 10 < armature["upper_frame"] <= 30)
                FORWARD = not own["HIT"]
            else:
                AIM = False
                FORWARD = True

            own["moving"] = True
            armature["FORWARD"] = FORWARD
            if own["left_right"] != 0:
                own["left_right"] = 0
            armature["LEFT"] = armature["RIGHT"] = LEFT = RIGHT = False

    armature["BACK"] = BACK = not FORWARD
    armature["AIM"] = AIM
    AI_motion.main(cont, own, FORWARD, BACK, LEFT, RIGHT, AIM)

def normal_state(cont, own, brain, armature, front_sensor):
    if front_sensor:
        armature["FORWARD"] = FORWARD = False
        if own["left_right"] == 0:
            own["left_right"] = randint(1,2)

        armature["LEFT"] = LEFT = own["left_right"] == 1
        armature["RIGHT"] = RIGHT = own["left_right"] == 2
    else:
        armature["FORWARD"] = FORWARD = own["moving"] = True
        if own["left_right"] != 0:
            own["left_right"] = 0

        armature["LEFT"] = armature["RIGHT"] = LEFT = RIGHT = False

    armature["BACK"] = BACK = not FORWARD
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
