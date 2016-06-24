from random import randint

def turn_left(own):
    own.applyRotation([0,0,0.01],True)

def turn_right(own):
    own.applyRotation([0,0,-0.01],True)

def move(own):
    if own["FORWARD"]:
        own.setLinearVelocity([-10,0,0], True)

def stop(own):

    own.setLinearVelocity([0.00000012,0,0])
    own["moving"] = False
    own.setLinearVelocity([0,0,0])

def main(cont):
    own = cont.owner

    brain = own["brain"]
    FORWARD = own["FORWARD"]
    RUN = own["RUN"]
    own["FALL"] = not own.children["AI_lower_sensor"]["collision"]
    moving = own["moving"]

    if not own["FALL"]:
        front_sensor = own.children["AI_front_sensor"]["collision"]

        if brain == 0:
            if not front_sensor:
                FORWARD = True
                moving = True
                if own["left_right"] != 0:
                    own["left_right"] = 0
            else:
                FORWARD = False
                if moving:
                    stop(own)
                if own["left_right"] == 0:
                    own["left_right"] = randint(1,2)
                elif own["left_right"] == 1:
                    turn_left(own)
                elif own["left_right"] == 2:
                    turn_right(own)

        elif brain == 1:
            if not front_sensor:
                FORWARD = True
                moving = True
                if own["left_right"] != 0:
                    own["left_right"] = 0
            else:
                FORWARD = False
                if moving:
                    stop(own)
                if own["left_right"] == 0:
                    own["left_right"] = randint(1,2)
                elif own["left_right"] == 1:
                    turn_left(own)
                elif own["left_right"] == 2:
                    turn_right(own)

        own["FORWARD"] = FORWARD
        own["moving"] = moving
        move(own)
