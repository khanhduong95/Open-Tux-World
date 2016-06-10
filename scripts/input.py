import bge

keyboard = bge.logic.keyboard
mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
ACTIVE = bge.logic.KX_INPUT_ACTIVE

def main(cont):
    own = cont.owner
    
    own["FORWARD"] = keyboard.events[bge.events.WKEY] == ACTIVE
    own["LEFT"] = keyboard.events[bge.events.AKEY] == ACTIVE
    own["BACK"] = keyboard.events[bge.events.SKEY] == ACTIVE
    own["RIGHT"] = keyboard.events[bge.events.DKEY] == ACTIVE

    own["JUMP"] = keyboard.events[bge.events.SPACEKEY] == ACTIVE
    own["RUN"] = keyboard.events[bge.events.LEFTSHIFTKEY] == ACTIVE or keyboard.events[bge.events.RIGHTSHIFTKEY] == ACTIVE
    
    own["AIM"] = mouse.events[bge.events.RIGHTMOUSE] == ACTIVE
    own["HIT"] = mouse.events[bge.events.LEFTMOUSE] == JUST_ACTIVATED
    