import bge
import math

mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

start_aim = 0
current_frame = 0

def main():

    global start_aim
    global current_frame
    cont = bge.logic.getCurrentController()
    cam = bge.logic.getCurrentScene().objects["Camera"]    
    cam_pos = bge.logic.getCurrentScene().objects["cam_pos"]    
    cam_dir = bge.logic.getCurrentScene().objects["cam_dir"]
    
    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
        cont.activate(cont.actuators["forward_dir"])
        cont.activate(cont.actuators["Mouse"])
        if start_aim == 0:
            bge.types.KX_MouseActuator.reset(bge.logic.getCurrentScene().objects["camera_track2"].actuators["Mouse"])            
            #cont.deactivate(cont.actuators["forward_dir"])
        if start_aim != 5:
#            cont.activate(cont.actuators["aim"])
            #cont.owner.applyMovement([-1,0,0],True)
            cam_dir.applyMovement([0,0.07,0],True)
            cam_dir.applyRotation([0,0,math.radians(0.3)],True)
            cam_pos.applyMovement([-1.2,0,0],True)
            #cont.owner.applyRotation([0,0,math.radians(0.2)],True)
            start_aim += 1
#        else:
#            cont.deactivate(cont.actuators["aim"])            
        
    elif mouse.events[bge.events.RIGHTMOUSE] == NONE:
        if start_aim == 5:
            bge.types.KX_MouseActuator.reset(bge.logic.getCurrentScene().objects["camera_track2"].actuators["Mouse"])            
        if start_aim != 0:
#            cont.activate(cont.actuators["stop_aim"])
            #cont.owner.applyMovement([1,0,0],True)
            cam_dir.applyMovement([0,-0.07,0],True)
            cam_dir.applyRotation([0,0,-math.radians(0.3)],True)
            cam_pos.applyMovement([1.2,0,0],True)
            #cont.owner.applyRotation([0,0,-math.radians(0.2)],True)
            start_aim -= 1

#        else:
#            cont.deactivate(cont.actuators["stop_aim"])                        