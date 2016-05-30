import bge
import math

mouse = bge.logic.mouse

#JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
#JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
#NONE = bge.logic.KX_INPUT_NONE

def main():

    cont = bge.logic.getCurrentController()
    act1 = cont.actuators["add_target_mark"]
    act2 = cont.actuators["remove_target_mark"]

    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
	    cont.activate(act1)
    else:
	    cont.activate(act2)

