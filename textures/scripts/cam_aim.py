from bge import logic, events

mouse = logic.mouse
ACTIVE = logic.KX_INPUT_ACTIVE
NONE = logic.KX_INPUT_NONE

def main(cont):
    own = cont.owner

    if not own["FALL"]:
        start_aim = own["start_aim"]
        cam_pos = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"]

        if mouse.events[events.RIGHTMOUSE] == ACTIVE:
            cont.activate(cont.actuators["forward_dir"])
            cont.activate(cont.actuators["Mouse"])

            if start_aim != 5:
                cam_pos.applyMovement([-1.5,0,0],True)
                start_aim += 1

        else:

            if start_aim != 0:
                cam_pos.applyMovement([1.5,0,0],True)
                start_aim -= 1

        own["start_aim"] = start_aim
