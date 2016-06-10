import bge

def aim_move(own):
    
    FORWARD = own["FORWARD"]
    LEFT = own["LEFT"]
    BACK = own["BACK"]
    RIGHT = own["RIGHT"]

    if LEFT:
        if FORWARD:
            own.setLinearVelocity([-7,-7,0],True)         
        
        elif BACK:
            own.setLinearVelocity([7,-7,0],True)         
                
        else:
            own.setLinearVelocity([0,-10,0],True)         
        
    if RIGHT:
        if FORWARD:
            own.setLinearVelocity([-7,7,0],True)         

        elif BACK:
            own.setLinearVelocity([7,7,0],True)         
                
        else:
            own.setLinearVelocity([0,10,0],True)         

    if FORWARD == True and LEFT == False and RIGHT == False and BACK == False:
        own.setLinearVelocity([-10,0,0],True)         

    if BACK == True and LEFT == False and RIGHT == False and FORWARD == False:
        own.setLinearVelocity([10,0,0],True)         

def normal_move(own):

    if own["RUN_FAST"]:
        if own["JUMP"]:
            own.setLinearVelocity([-30,0,20],True) 
        else:
            own.setLinearVelocity([-30,0,0],True) 
    elif own["RUN"]:
        if own["JUMP"]:
            own.setLinearVelocity([-20,0,20],True) 
        else:
            own.setLinearVelocity([-20,0,0],True) 
    else:
        if own["JUMP"]:
            own.setLinearVelocity([-10,0,20],True) 
        else:
            own.setLinearVelocity([-10,0,0],True) 

def stop(own):
    
    own.setLinearVelocity([0.00000012,0,0]) 
    own["moving"] = False 
    own.setLinearVelocity([0,0,0]) 

def move(cont):    

    own = cont.owner
    
    FORWARD = own["FORWARD"]
    LEFT = own["LEFT"]
    BACK = own["BACK"]
    RIGHT = own["RIGHT"]
                    
    if LEFT:
        if FORWARD:
            cont.activate(cont.actuators["for_left_dir"])
        
        elif BACK:
            cont.activate(cont.actuators["back_left_dir"])
                
        else:
            cont.activate(cont.actuators["left_dir"])
        
    if RIGHT:
        if FORWARD:
            cont.activate(cont.actuators["for_right_dir"])

        elif BACK:
            cont.activate(cont.actuators["back_right_dir"])
                
        else:
            cont.activate(cont.actuators["right_dir"])

    if FORWARD == True and LEFT == False and RIGHT == False and BACK == False:
        cont.activate(cont.actuators["forward_dir"])

    if BACK == True and LEFT == False and RIGHT == False and FORWARD == False:
        cont.activate(cont.actuators["backward_dir"])

    cont.activate(cont.actuators["Mouse"])
    normal_move(own)
    
def main(cont):
    
    own = cont.owner

    cont.deactivate(cont.actuators["Mouse"])    
    cont.deactivate(cont.actuators["forward_dir"])
    cont.deactivate(cont.actuators["backward_dir"])
    cont.deactivate(cont.actuators["left_dir"])
    cont.deactivate(cont.actuators["right_dir"])
    cont.deactivate(cont.actuators["for_left_dir"])
    cont.deactivate(cont.actuators["for_right_dir"])
    cont.deactivate(cont.actuators["back_left_dir"])
    cont.deactivate(cont.actuators["back_right_dir"])    
    
    sun_moon = bge.logic.getCurrentScene().objects["sun_moon_holder_parent"]
    sun_moon.worldPosition.x = own.worldPosition.x   
    sun_moon.worldPosition.y = own.worldPosition.y   

    own["FALL"] = own.children["lower_cube"]["collision"] == False

    if own["FALL"] == False:
        own["RUN_FAST"] = own["RUN"] and own["stamina"] >= 1
            
        if own["AIM"]:
            own["moving"] = True
            aim_move(own)
                
        else:
            if own["FORWARD"] or own["BACK"] or own["LEFT"] or own["RIGHT"]:
                own["moving"] = True
                move(cont)
            
            elif own["JUMP"]:
                own.setLinearVelocity([0,0,20],True)
            
            elif own["moving"]:
                stop(own)
            
