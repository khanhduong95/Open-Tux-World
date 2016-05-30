import bge
from bge import logic

mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

def main():
    cont = logic.getCurrentController()
    #cam = cont.owner
    scene = logic.getCurrentScene()
    
    cam = scene.objects["Camera"]
    target = scene.objects["cam_pos"]
    
#    if mouse.events[bge.events.RIGHTMOUSE] == ACTIVE:
#        target = scene.objects["cam_pos_aim"]
        
    ray = cont.sensors["cam_ray"]
    
    if ray.positive:
        cam.worldPosition = ray.hitPosition
    
    else:
        cam.worldPosition = target.worldPosition
