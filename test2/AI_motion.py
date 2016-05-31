import bge
from random import randint

def turn_left(own):
    own.applyRotation([0,0,0.01],True)

def turn_right(own):
    own.applyRotation([0,0,-0.01],True)
    
def move(own):
    if own["MOVE"] == True:
        own.children["AI_Armature"]["FORWARD"] = True
        own.applyMovement([-0.03,0,0], True)    
    else:
        own.children["AI_Armature"]["FORWARD"] = False
    
def main(cont):
    own = cont.owner

    brain = own["brain"]
    MOVE = own["MOVE"]
    RUN = own["RUN"]
    if own.sensors["Collision"].positive:
        front_sensor = own.children["AI_front_sensor"]["collision"]
        lower_sensor = own.children["AI_lower_sensor"]["collision"]
        own.children["AI_Armature"]["FALL"] = False
        
        if brain == 0:
            if front_sensor == False and lower_sensor == True: 
                MOVE = True
                if own["left_right"] != 0:
                    own["left_right"] = 0
            else:
                MOVE = False
                if own["left_right"] == 0:
                    own["left_right"] = randint(1,2)
                elif own["left_right"] == 1:
                    turn_left(own)
                elif own["left_right"] == 2:
                    turn_right(own)

        elif brain == 1:
            if front_sensor == False and lower_sensor == True: 
                MOVE = True
                if own["left_right"] != 0:
                    own["left_right"] = 0
            else:
                MOVE = False
                if own["left_right"] == 0:
                    own["left_right"] = randint(1,2)
                elif own["left_right"] == 1:
                    turn_left(own)
                elif own["left_right"] == 2:
                    turn_right(own)
        
        own["MOVE"] = MOVE    
        move(own)
#    print(brain)
    else:
        own.children["AI_Armature"]["FALL"] = True