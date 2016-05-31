import bge
import math

def move(own):
    current_frame = own["current_frame"]
    FORWARD = own["FORWARD"]
    BACK = own["BACK"]
    LEFT = own["LEFT"]
    RIGHT = own["RIGHT"]
    RUN = own["RUN"]
    
    if FORWARD == True or BACK == True or LEFT == True or RIGHT == True:
        #cont = bge.logic.getCurrentController()
        if RUN == True:
            if current_frame <= 0:
                current_frame = 0
            if current_frame >= 42:
                current_frame = 14 
            own.playAction("AI_run", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
            current_frame += 1            
        else:
            if current_frame <= 0:
                current_frame = 0
            if current_frame >= 77:
                current_frame = 7 
            own.playAction("AI_walk", current_frame, current_frame+1, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
            current_frame += 1
                
    else:
        #cont = bge.logic.getCurrentController()
        own.playAction("AI_walk", 0, 0, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
        current_frame = 0
    own["current_frame"] = current_frame
    
def fall(own):
    current_frame = own["current_frame"]
    own.playAction("AI_fall", 7, 7, layer=0, play_mode=bge.logic.KX_ACTION_MODE_PLAY)
    current_frame = 0
    own["current_frame"] = current_frame

def main(cont):
    own = cont.owner
    FALL = own["FALL"]
    if FALL == True:
        fall(own)
    else:
        move(own)    