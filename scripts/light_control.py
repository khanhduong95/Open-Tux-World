import bge

keyboard = bge.logic.keyboard
mouse = bge.logic.mouse

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
JUST_RELEASED = bge.logic.KX_INPUT_JUST_RELEASED
ACTIVE = bge.logic.KX_INPUT_ACTIVE
NONE = bge.logic.KX_INPUT_NONE

daytime = True
hour = 12
minute = 0

def main():
    co = bge.logic.getCurrentController()
    sun = bge.logic.getCurrentScene().objects["sun"]
    moon = bge.logic.getCurrentScene().objects["moon"]
    sun_sky = bge.logic.getCurrentScene().objects["sun_sky"]
    moon_sky = bge.logic.getCurrentScene().objects["moon_sky"]

#    toggle = co.sensors["space"]
    
    delay = co.sensors["Delay"]
        
    global hour
    global minute
    global daytime    
    
    if delay.positive:
        minute += 1
        co.activate(co.actuators["Motion"])
            
    if minute == 60:
        minute = 0
        hour += 1
    
    if hour == 24:
        hour = 0
        
    if hour < 6 or hour > 18:
        daytime = False
        
    if hour >= 6 and hour <= 18:
        daytime = True
                     
#    if toggle.positive:
    if daytime == True:
        moon.energy = 0.0
        sun.energy = 1.0
        moon_sky.energy = 0.0
        sun_sky.energy = 1.0
#            daytime = False
#        else:
    if daytime == False: 
        moon.energy = 0.05
        sun.energy = 0.0
        moon_sky.energy = 0.05
        sun_sky.energy = 0.0
#            daytime = True
