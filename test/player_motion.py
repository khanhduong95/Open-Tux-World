import bge
import math
from mathutils import Vector

keyboard = bge.logic.keyboard
mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

#character = logic.getCurrentScene().objects['body']

rotated_z = 0

FORWARD = False
LEFT = False
RIGHT = False
BACK = False

def move():    
    
    global rotated_z
                    
    if LEFT == True:
        if FORWARD == True:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(-45)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)
                    rotated_z += rot_angle
                    
        
        elif BACK == True:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(-135)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)                        
                    #global rotated_z
                    rotated_z += rot_angle
                
        else:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(-90)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)
                    #global rotated_z
                    rotated_z += rot_angle

        bge.logic.getCurrentController().owner.localPosition += bge.logic.getCurrentController().owner.localOrientation * Vector([-0.4,0,0])
        
    if RIGHT == True:
        if FORWARD == True:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(45)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)
                    #global rotated_z
                    rotated_z += rot_angle

        elif BACK == True:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(135)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)                        
                    #global rotated_z
                    rotated_z += rot_angle
                
        else:
            cam = bge.logic.getCurrentScene().objects["camera_track"]
            rot_cam = cam.localOrientation.to_euler()
            cont = bge.logic.getCurrentController()
            rot_cont = cont.owner.localOrientation.to_euler()
            angle = (rot_cam.z - math.radians(90)) - rot_cont.z
            rot_angle = angle/100
            if rot_angle !=0:
                for x in range(0, 100):
                    cont.owner.applyRotation([0, 0, rot_angle], False)
                    #global rotated_z
                    rotated_z += rot_angle

        bge.logic.getCurrentController().owner.localPosition += bge.logic.getCurrentController().owner.localOrientation * Vector([-0.4,0,0])


    if FORWARD == True and LEFT == False and RIGHT == False and BACK == False:
        cam = bge.logic.getCurrentScene().objects["camera_track"]
        rot_cam = cam.localOrientation.to_euler()
        cont = bge.logic.getCurrentController()
        rot_cont = cont.owner.localOrientation.to_euler()
        angle = (rot_cam.z - math.radians(0)) - rot_cont.z
        rot_angle = angle/100
        if rot_angle !=0:
            for x in range(0, 100):
                cont.owner.applyRotation([0, 0, rot_angle], False)
                #global rotated_z
                rotated_z += rot_angle

        bge.logic.getCurrentController().owner.localPosition += bge.logic.getCurrentController().owner.localOrientation * Vector([-0.4,0,0])

    if BACK == True and LEFT == False and RIGHT == False and FORWARD == False:
        cam = bge.logic.getCurrentScene().objects["camera_track"]
        rot_cam = cam.localOrientation.to_euler()
        cont = bge.logic.getCurrentController()
        rot_cont = cont.owner.localOrientation.to_euler()
        angle = (rot_cam.z - math.radians(180)) - rot_cont.z
        rot_angle = angle/100
        if rot_angle !=0:
            for x in range(0, 100):
                cont.owner.applyRotation([0, 0, rot_angle], False)
                #global rotated_z
                rotated_z += rot_angle

        bge.logic.getCurrentController().owner.localPosition += bge.logic.getCurrentController().owner.localOrientation * Vector([-0.4,0,0])

#def rotated_z():
#    return rotated_z
        
def main():
    
    global FORWARD
    global LEFT
    global BACK
    global RIGHT
            
    if keyboard.events[bge.events.WKEY] == JUST_ACTIVATED or keyboard.events[bge.events.WKEY] == ACTIVE:
        FORWARD = True
    if keyboard.events[bge.events.WKEY] == JUST_RELEASED:
        FORWARD = False
    if keyboard.events[bge.events.AKEY] == JUST_ACTIVATED or keyboard.events[bge.events.AKEY] == ACTIVE:
        LEFT = True
    if keyboard.events[bge.events.AKEY] == JUST_RELEASED:
        LEFT = False
    if keyboard.events[bge.events.SKEY] == JUST_ACTIVATED or keyboard.events[bge.events.SKEY] == ACTIVE:
    	BACK = True
    if keyboard.events[bge.events.SKEY] == JUST_RELEASED:
       	BACK = False
    if keyboard.events[bge.events.DKEY] == JUST_ACTIVATED or keyboard.events[bge.events.DKEY] == ACTIVE:
    	RIGHT = True
    if keyboard.events[bge.events.DKEY] == JUST_RELEASED:
    	RIGHT = False
    move()
    return rotated_z