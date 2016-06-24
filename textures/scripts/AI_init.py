from bge import logic
from random import randint

def main(cont):
    own = cont.owner
    try:
        ID = logic.globalDict['ID'] = logic.globalDict['ID'] + 1

    except:
        ID = logic.globalDict['ID'] = 0

    own['ID'] = ID
    own['brain'] = randint(0,1)
    own.state = logic.KX_STATE2