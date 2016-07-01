from bge import logic
from random import randint

def main(cont):
    own = cont.owner
    brain = own["brain"] = randint(0,1)
    if brain == 1:
        snow_ice = randint(0,2)
        if snow_ice == 1:
            own["snow"] = 20
        elif snow_ice == 2:
            own["ice"] = 20

    own.state = logic.KX_STATE2