def check_ray(own, ray):
    cam = own.children["cam_holder"]
    target = own.children["cam_pos"]
    if ray.positive:
        cam.worldPosition = ray.hitPosition
    else:
        cam.worldPosition = target.worldPosition

def main(cont):
    own = cont.owner
    if own.state == 1:
        check_ray(own, cont.sensors["cam_ray"])
    else:
        check_ray(own, cont.sensors["cam_ray.001"])
