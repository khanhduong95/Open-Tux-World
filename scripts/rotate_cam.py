import bge
import math

def main(cont):
    own = cont.owner
    cam_dir = own.children["cam_dir2"]
    rot = cam_dir["rotation"]    
    
    if own["collision"] == True:
        if rot < 10:
            cam_dir.applyRotation([0,0,-math.radians(0.4)],True)
            rot += 1
    else:
        if rot > 0:
            cam_dir.applyRotation([0,0,math.radians(0.4)],True)
            rot -= 1
    
    cam_dir["rotation"] = rot     
        