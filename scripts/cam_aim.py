import bge
import math

mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

def main(cont):
    own = cont.owner

    if own["FALL"] == False:
        start_aim = own["start_aim"]
    
        cam_pos = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"]
    
        if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
            cont.activate(cont.actuators["forward_dir"])
            cont.activate(cont.actuators["Mouse"])
            if start_aim == 0:
                bge.types.KX_MouseActuator.reset(own.children["camera_track"].children["camera_track2"].actuators["Mouse"])             
    
            if start_aim != 5:
                cam_pos.applyMovement([-1.5,0,0],True)
                start_aim += 1
            
        elif mouse.events[bge.events.RIGHTMOUSE] == NONE:
            if start_aim == 5:
                bge.types.KX_MouseActuator.reset(own.children["camera_track"].children["camera_track2"].actuators["Mouse"])            
            if start_aim != 0:
                cam_pos.applyMovement([1.5,0,0],True)
                start_aim -= 1

        own["start_aim"] = start_aim            
