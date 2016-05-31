import bge

def main(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    if col.positive:
        own["collision"] = True
    else:
        own["collision"] = False