import bge
import math
from mathutils import Vector

#character = logic.getCurrentScene().objects['body']

TARGET = True

def to_normal_state():
    if TARGET == False:
        cont = bge.logic.getCurrentController()
        cam = bge.logic.getCurrentScene().objects["Camera"]

        bge.types.KX_MouseActuator.reset(bge.logic.getCurrentScene().objects["body"].actuators["Mouse"])
        bge.types.KX_MouseActuator.reset(bge.logic.getCurrentScene().objects["camera_track2"].actuators["Mouse"])
        
        bge.logic.getCurrentScene().active_camera = cam
        
        act = cont.actuators["to_normal_view"]
        cont.activate(act)

def main():
    global TARGET

    cont = bge.logic.getCurrentController()
    sen = cont.sensors["rmb1"]
    if sen.positive == False:
    	TARGET = False
    to_normal_state()