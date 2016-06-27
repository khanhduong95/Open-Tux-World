from bge import logic

def main(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    hit = scene.addObject("hit",own,2)
    hit["owner_ID"] = own.parent["ID"]
    hit.setLinearVelocity([-90,0,0], True)
    own.parent["hit_released"] = False
