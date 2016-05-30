import bge
import math

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

max_stamina = 400
stamina = max_stamina
stamina_timer = 0

current_frame = 0
upper_frame = 0
started_aim = 0

def aim_move():
    global current_frame
    global started_aim
    
    if bge.logic.getCurrentScene().objects["Cube"].sensors["Collision"].positive: 
        if FORWARD == True:
            if LEFT == True:
                cont = bge.logic.getCurrentController()
                if current_frame <= 70:
                    current_frame = 70
                if current_frame >= 120:
                    current_frame = 80 
                cont.owner.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 1
            elif RIGHT == True:
                cont = bge.logic.getCurrentController()
                if current_frame <= 130:
                    current_frame = 130
                if current_frame >= 180:
                    current_frame = 140 
                cont.owner.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 1
            else:
                cont = bge.logic.getCurrentController()
                if current_frame <= 10:
                    current_frame = 10
                if current_frame >= 60:
                    current_frame = 20 
                cont.owner.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 1

        elif BACK == True:
            if LEFT == True:
                cont = bge.logic.getCurrentController()
                if current_frame >= 190:
                    current_frame = 190
                if current_frame <= 140:
                    current_frame = 180 
                cont.owner.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame -= 1
            elif RIGHT == True:
                cont = bge.logic.getCurrentController()
                if current_frame >= 130:
                    current_frame = 130
                if current_frame <= 80:
                    current_frame = 120 
                cont.owner.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame -= 1
            else:
                cont = bge.logic.getCurrentController()
                if current_frame >= 70:
                    current_frame = 70
                if current_frame <= 20:
                    current_frame = 60 
                cont.owner.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame -= 1
        
        elif LEFT == True and RIGHT == False and FORWARD == False and BACK == False:
            cont = bge.logic.getCurrentController()
            if current_frame >= 250:
                current_frame = 250
            if current_frame <= 200:
                current_frame = 240 
            cont.owner.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
            current_frame -= 1
                    
        elif RIGHT == True and LEFT == False and FORWARD == False and BACK == False:
            cont = bge.logic.getCurrentController()
            if current_frame <= 190:
                current_frame = 190
            if current_frame >= 240:
                current_frame = 200 
            cont.owner.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
            current_frame += 1
                
        else:
            cont = bge.logic.getCurrentController()
            if started_aim == 0:
                #cont.owner.stopAction()
                cont.owner.playAction("lower_aim", 0, 10, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                #current_frame = 10
                started_aim = 1
            else:
                #cont.owner.stopAction()
                cont.owner.playAction("lower_aim", 10, 10, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                #current_frame = 10
                    
    else:
        cont = bge.logic.getCurrentController()
        #cont.owner.stopAction()
        cont.owner.playAction("fall", 7, 7, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
        #current_frame = 10
        started_aim = 0

def move():
    global current_frame
    
    if bge.logic.getCurrentScene().objects["Cube"].sensors["Collision"].positive: 
        if FORWARD == True or BACK == True or LEFT == True or RIGHT == True:
            cont = bge.logic.getCurrentController()
            if RUN_FAST == True:
                if current_frame <= 0:
                    current_frame = 0
                if current_frame >= 42:
                    current_frame = 14 
                cont.owner.playAction("run", current_frame, current_frame+2, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 2            
            elif RUN == True:
                if current_frame <= 0:
                    current_frame = 0
                if current_frame >= 42:
                    current_frame = 14 
                cont.owner.playAction("run", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 1            
            else:
                if current_frame <= 0:
                    current_frame = 0
                if current_frame >= 77:
                    current_frame = 7 
                cont.owner.playAction("walk", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                current_frame += 1
                
        else:
            cont = bge.logic.getCurrentController()
            #cont.owner.stopAction()
            cont.owner.playAction("walk", 0, 0, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
            current_frame = 0
    
    else:
        cont = bge.logic.getCurrentController()
        #cont.owner.stopAction()
        cont.owner.playAction("fall", 7, 7, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
        current_frame = 0

def action():
    
    global upper_frame
    
    cont = bge.logic.getCurrentController()
    
    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
        if mouse.events[bge.events.LEFTMOUSE] == JUST_ACTIVATED:
            cont.owner.playAction("upper_aim", 10, 20, layer=2, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
        else:        
            if upper_frame >= 10:
                cont.owner.playAction("upper_aim", 10, 10, layer=1, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                upper_frame = 10
            else:
                cont.owner.playAction("upper_aim", upper_frame, upper_frame+1, layer=1, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                upper_frame += 1

    if mouse.events[bge.events.RIGHTMOUSE] == NONE:    
        if mouse.events[bge.events.LEFTMOUSE] == JUST_ACTIVATED:
            cont.owner.playAction("upper_aim", 10, 20, layer=2, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
        else:
            if upper_frame <= 0:
                cont.owner.playAction("upper_aim", 0, 0, layer=1, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                upper_frame = 0
            else:
                cont.owner.playAction("upper_aim", upper_frame, upper_frame-1, layer=1, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
                upper_frame -= 1

def main():
    
    global FORWARD
    global LEFT
    global BACK
    global RIGHT
    global RUN
    global RUN_FAST
    global stamina
    global stamina_timer
    
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
        if stamina == 0:
            RUN_FAST = False
            RUN = True
        else:
            RUN = False
            RUN_FAST = True
            stamina -= 1
        stamina_timer = 0
                
    if keyboard.events[bge.events.LEFTSHIFTKEY] == NONE and keyboard.events[bge.events.RIGHTSHIFTKEY] == NONE:
        RUN = False
        RUN_FAST = False

        if stamina_timer < 300:
            stamina_timer += 1
    
    if stamina_timer == 300:
        stamina = max_stamina

#    if keyboard.events[bge.events.RKEY] == ACTIVE:
#    	RUN_FAST = True
#    if keyboard.events[bge.events.RKEY] == NONE:
#    	RUN_FAST = False
    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
        aim_move()
    if mouse.events[bge.events.RIGHTMOUSE] == NONE:    
        move()        
        