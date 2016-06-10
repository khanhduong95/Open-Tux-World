import bge
from bge import logic

mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

def main(cont):
    own = cont.owner
    
#    cam = own.children["cam_dir"].children["cam_holder"]
#    target = own.children["cam_dir"].children["cam_pos"]

    cam = own.children["cam_holder"]
    target = own.children["cam_pos"]
    
    ray = cont.sensors["cam_ray"]
    
    if ray.positive:
        cam.worldPosition = ray.hitPosition
    
    else:
        cam.worldPosition = target.worldPosition
