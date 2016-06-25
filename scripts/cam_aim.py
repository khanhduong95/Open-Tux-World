from bge import logic, events

def main(cont):
    own = cont.owner
    start_aim = own["start_aim"]
    cam_pos = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"]
    if not own["FALL"] and  logic.mouse.events[events.RIGHTMOUSE] == logic.KX_INPUT_ACTIVE:
        cont.activate(cont.actuators["forward_dir"])
        cont.activate(cont.actuators["Mouse"])
        if start_aim != 8:
            cam_pos.applyMovement([-1.5,0,0],True)
            start_aim += 1

    elif start_aim != 0:
        cam_pos.applyMovement([1.5,0,0],True)
        start_aim -= 1

    own["start_aim"] = start_aim
