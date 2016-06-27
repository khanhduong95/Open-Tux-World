from bge import logic

def main(cont):
    own = cont.owner
    try:
        distance = own.getDistanceTo(logic.getCurrentScene().objects["player_loc"])
        if distance >= 250:
            own.endObject()
    except:
        own.endObject()
