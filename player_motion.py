import bge
import math
from mathutils import Vector

keyboard = bge.logic.keyboard
mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

FORWARD = False
LEFT = False
RIGHT = False
BACK = False
RUN = False
RUN_FAST = False

def aim_move():
    if LEFT == True:
        if FORWARD == True:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([-0.11,-0.11,0], True)
        
        elif BACK == True:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([0.11,-0.11,0], True)
                
        else:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([0,-0.15,0], True)
        
    if RIGHT == True:
        if FORWARD == True:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([-0.11,0.11,0], True)

        elif BACK == True:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([0.11,0.11,0], True)
                
        else:
            cont = bge.logic.getCurrentController()
            cont.owner.applyMovement([0,0.15,0], True)

    if FORWARD == True and LEFT == False and RIGHT == False and BACK == False:
        cont = bge.logic.getCurrentController()
        cont.owner.applyMovement([-0.15,0,0], True)

    if BACK == True and LEFT == False and RIGHT == False and FORWARD == False:
        cont = bge.logic.getCurrentController()
        cont.owner.applyMovement([0.15,0,0], True)

def move():    
                    
    if LEFT == True:
        if FORWARD == True:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["for_left_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)
        
        elif BACK == True:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["back_left_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)
                
        else:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["left_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)
        
    if RIGHT == True:
        if FORWARD == True:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["for_right_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)

        elif BACK == True:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["back_right_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)
                
        else:
            cont = bge.logic.getCurrentController()
            act = cont.actuators["right_dir"]
            cont.activate(act)
            if RUN_FAST == True:
                cont.owner.applyMovement([-0.5,0,0], True)
            elif RUN == True:
                cont.owner.applyMovement([-0.3,0,0], True)
            else:    
                cont.owner.applyMovement([-0.15,0,0], True)

    if FORWARD == True and LEFT == False and RIGHT == False and BACK == False:
        cont = bge.logic.getCurrentController()
        act = cont.actuators["forward_dir"]
        cont.activate(act)
        if RUN_FAST == True:
            cont.owner.applyMovement([-0.5,0,0], True)
        elif RUN == True:
            cont.owner.applyMovement([-0.3,0,0], True)
        else:    
            cont.owner.applyMovement([-0.15,0,0], True)

    if BACK == True and LEFT == False and RIGHT == False and FORWARD == False:
        cont = bge.logic.getCurrentController()
        act = cont.actuators["backward_dir"]
        cont.activate(act)
        if RUN_FAST == True:
            cont.owner.applyMovement([-0.5,0,0], True)
        elif RUN == True:
            cont.owner.applyMovement([-0.3,0,0], True)
        else:    
            cont.owner.applyMovement([-0.15,0,0], True)

def main():
    
    global FORWARD
    global LEFT
    global BACK
    global RIGHT
    global RUN
    global RUN_FAST

    cont = bge.logic.getCurrentController()
    act_forward = cont.actuators["forward_dir"]
    act_backward = cont.actuators["backward_dir"]
    act_left = cont.actuators["left_dir"]
    act_right = cont.actuators["right_dir"]
    act_for_left = cont.actuators["for_left_dir"]
    act_for_right = cont.actuators["for_right_dir"]
    act_back_left = cont.actuators["back_left_dir"]
    act_back_right = cont.actuators["back_right_dir"]
    cont.deactivate(act_forward)
    cont.deactivate(act_backward)
    cont.deactivate(act_left)
    cont.deactivate(act_right)
    cont.deactivate(act_for_left)
    cont.deactivate(act_for_right)
    cont.deactivate(act_back_left)
    cont.deactivate(act_back_right)    
        
    if keyboard.events[bge.events.WKEY] == ACTIVE:
        FORWARD = True
    if keyboard.events[bge.events.WKEY] == NONE:
        FORWARD = False
    if keyboard.events[bge.events.AKEY] == ACTIVE:
        LEFT = True
    if keyboard.events[bge.events.AKEY] == NONE:
        LEFT = False
    if keyboard.events[bge.events.SKEY] == ACTIVE:
    	BACK = True
    if keyboard.events[bge.events.SKEY] == NONE:
       	BACK = False
    if keyboard.events[bge.events.DKEY] == ACTIVE:
    	RIGHT = True
    if keyboard.events[bge.events.DKEY] == NONE:
    	RIGHT = False
    if keyboard.events[bge.events.LEFTSHIFTKEY] == ACTIVE or keyboard.events[bge.events.RIGHTSHIFTKEY] == ACTIVE:
    	RUN = True
    if keyboard.events[bge.events.LEFTSHIFTKEY] == NONE and keyboard.events[bge.events.RIGHTSHIFTKEY] == NONE:
    	RUN = False
    if keyboard.events[bge.events.RKEY] == ACTIVE:
    	RUN_FAST = True
    if keyboard.events[bge.events.RKEY] == NONE:
    	RUN_FAST = False
    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
        aim_move()    
    if mouse.events[bge.events.RIGHTMOUSE] == NONE:
        move()
