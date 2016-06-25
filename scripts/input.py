from bge import logic, events

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
    own["FORWARD"] = keyboard.events[events.WKEY] == ACTIVE
    own["LEFT"] = keyboard.events[events.AKEY] == ACTIVE
    own["BACK"] = keyboard.events[events.SKEY] == ACTIVE
    own["RIGHT"] = keyboard.events[events.DKEY] == ACTIVE
    own["JUMP"] = keyboard.events[events.SPACEKEY] == ACTIVE
    own["RUN"] = keyboard.events[events.LEFTSHIFTKEY] == ACTIVE or keyboard.events[events.RIGHTSHIFTKEY] == ACTIVE
    own["AIM"] = mouse.events[events.RIGHTMOUSE] == ACTIVE
    own["HIT"] = mouse.events[events.LEFTMOUSE] == JUST_ACTIVATED