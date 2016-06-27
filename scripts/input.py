from bge import logic, events
from scripts import player_motion

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
    AIM = armature["AIM"] = mouse.events[events.RIGHTMOUSE] == ACTIVE
    own["HIT"] = mouse.events[events.LEFTMOUSE] == JUST_ACTIVATED
    player_motion.main(cont, own, FORWARD, BACK, LEFT, RIGHT, JUMP, AIM, FALL)
    print(id(own))