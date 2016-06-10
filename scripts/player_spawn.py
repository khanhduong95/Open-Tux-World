import bge

def main(cont):
    own = cont.owner
    
    if own["init"] == True:
        cont.activate(cont.actuators["spawn"])
        own["init"] = False
        cont.deactivate(cont.actuators["spawn"])
        