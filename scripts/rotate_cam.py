import math

def aim(rot_aim, cam_dir, collision, aim):
    if aim:
        if collision:
            if rot_aim < 10:
                cam_dir.applyRotation([0,0,math.radians(-0.25)],True)
                rot_aim += 1
        else:
            if rot_aim > 0:
                cam_dir.applyRotation([0,0,math.radians(0.25)],True)
                rot_aim -= 1
    else:
        if rot_aim < 5:
            cam_dir.applyRotation([0,0,math.radians(-0.25)],True)
            rot_aim += 1
        elif rot_aim > 5:
            cam_dir.applyRotation([0,0,math.radians(0.25)],True)
            rot_aim -= 1

    cam_dir["rot_aim"] = rot_aim

def main(cont):
    own = cont.owner
    cam_dir = own.children["cam_dir2"]
    rot = cam_dir["rot"]
    rot_aim = cam_dir["rot_aim"]
    col = own["collision"]
    if col:
        if rot < 10:
            cam_dir.applyRotation([0,0,math.radians(-0.4)],True)
            rot += 1
    else:
        if rot > 0:
            cam_dir.applyRotation([0,0,math.radians(0.4)],True)
            rot -= 1

    aim(rot_aim, cam_dir, col, own.parent.parent.children["Armature"]["AIM"])
    cam_dir["rot"] = rot