import bge
import math
from mathutils import Vector

TARGET = False

def to_target_state():
    if TARGET == True:
        cont = bge.logic.getCurrentController()
        #cam = bge.logic.getCurrentScene().objects["Camera"]
        target_cam = bge.logic.getCurrentScene().objects["target_camera"]

        bge.types.KX_MouseActuator.reset(bge.logic.getCurrentScene().objects["camera_track"].actuators["Mouse"])
        
        bge.logic.getCurrentScene().active_camera = target_cam
        
        act = cont.actuators["to_target_view"]
        cont.activate(act)

def main():
    global TARGET

    cont = bge.logic.getCurrentController()
    sen = cont.sensors["rmb"]
    if sen.positive:
    	TARGET = True
    to_target_state()