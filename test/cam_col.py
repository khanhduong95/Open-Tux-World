from bge import logic

def main():
    cont = logic.getCurrentController()
    #cam = cont.owner
    scene = logic.getCurrentScene()
    
    cam = scene.objects["Camera"]
    target = scene.objects["cam_pos"]
    ray = cont.sensors["cam_ray"]
        
    if ray.positive:
        cam.worldPosition = ray.hitPosition
    
    else:
        cam.worldPosition = target.worldPosition
