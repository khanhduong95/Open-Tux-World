def main(cont):
    own = cont.owner
    cam = own.children["cam_holder"]
    target = own.children["cam_pos"]
    ray = cont.sensors["cam_ray"]

    if ray.positive:
        cam.worldPosition = ray.hitPosition

    else:
        cam.worldPosition = target.worldPosition
