from bge import logic

def main(cont):
    own = cont.owner
    if own.parent["weapon"] == 0:
        hit = logic.getCurrentScene().addObject("hit",own,3)
        hit["owner_ID"] = own.parent["ID"]
        hit.setLinearVelocity([-45,0,0], True)
        own.parent["hit_released"] = False
