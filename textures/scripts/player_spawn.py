def main(cont):
    own = cont.owner

    if own["init"]:
        cont.activate(cont.actuators["spawn"])
        own["init"] = False
        cont.deactivate(cont.actuators["spawn"])