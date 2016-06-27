from bge import logic

def aim_move(own, FORWARD, BACK, LEFT, RIGHT):

    if LEFT:
        if FORWARD:
            own.setLinearVelocity([-7,-7,0],True)

        elif BACK:
            own.setLinearVelocity([7,-7,0],True)

        else:
            own.setLinearVelocity([0,-10,0],True)

    elif RIGHT:
        if FORWARD:
            own.setLinearVelocity([-7,7,0],True)

        elif BACK:
            own.setLinearVelocity([7,7,0],True)

        else:
            own.setLinearVelocity([0,10,0],True)

    elif FORWARD:
        own.setLinearVelocity([-10,0,0],True)

    elif BACK:
        own.setLinearVelocity([10,0,0],True)

def normal_move(own, RUN_FAST, RUN, JUMP):
    if RUN_FAST:
        if JUMP:
            own.setLinearVelocity([-30,0,6],True)
        else:
            own.setLinearVelocity([-30,0,0],True)
    elif RUN:
        if JUMP:
            own.setLinearVelocity([-20,0,6],True)
        else:
            own.setLinearVelocity([-20,0,0],True)
    else:
        if JUMP:
            own.setLinearVelocity([-10,0,6],True)
        else:
            own.setLinearVelocity([-10,0,0],True)

def stop(own):
    own.setLinearVelocity([0.00000012,0,0])
    own["moving"] = False
    own.setLinearVelocity([0,0,0])

def move(cont, FORWARD, BACK, LEFT, RIGHT, RUN_FAST, JUMP):
    if LEFT:
        if FORWARD:
            cont.activate(cont.actuators["for_left_dir"])

        elif BACK:
            cont.activate(cont.actuators["back_left_dir"])

        else:
            cont.activate(cont.actuators["left_dir"])

    elif RIGHT:
        if FORWARD:
            cont.activate(cont.actuators["for_right_dir"])

        elif BACK:
            cont.activate(cont.actuators["back_right_dir"])

        else:
            cont.activate(cont.actuators["right_dir"])

    elif FORWARD:
        cont.activate(cont.actuators["forward_dir"])

    elif BACK:
        cont.activate(cont.actuators["backward_dir"])

    cont.activate(cont.actuators["Mouse"])
    own = cont.owner
    normal_move(own, RUN_FAST, own["RUN"], JUMP)

def main(cont, own, FORWARD, BACK, LEFT, RIGHT, JUMP, AIM, FALL):
    cont.deactivate(cont.actuators["Mouse"])
    cont.deactivate(cont.actuators["forward_dir"])
    cont.deactivate(cont.actuators["backward_dir"])
    cont.deactivate(cont.actuators["left_dir"])
    cont.deactivate(cont.actuators["right_dir"])
    cont.deactivate(cont.actuators["for_left_dir"])
    cont.deactivate(cont.actuators["for_right_dir"])
    cont.deactivate(cont.actuators["back_left_dir"])
    cont.deactivate(cont.actuators["back_right_dir"])

    #obj_list = logic.getCurrentScene().objects
    #obj_list["player_loc"].worldPosition = own.worldPosition
    sun_moon = logic.getCurrentScene().objects["sun_moon_holder_parent"]
    sun_moon.worldPosition.x = own.worldPosition.x
    sun_moon.worldPosition.y = own.worldPosition.y

    if FALL:
        own.state = logic.KX_STATE3
    else:
        own.worldOrientation[2] = [ 0.0, 0.0, 1.0 ]
        RUN_FAST = own.children["Armature"]["RUN_FAST"] = own["RUN"] and own["stamina"] >= 1

        if FORWARD or BACK or LEFT or RIGHT:
            own["moving"] = True
            if AIM:
                aim_move(own, FORWARD, BACK, LEFT, RIGHT)

            else:
                move(cont, FORWARD, BACK, LEFT, RIGHT, RUN_FAST, JUMP)

        elif JUMP:
            own.setLinearVelocity([0,0,6],True)

        elif own["moving"]:
            stop(own)
