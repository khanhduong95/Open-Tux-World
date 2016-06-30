from bge import logic

def shoot_setup(own, scene, name, name_inventory, mass):
    own.parent["hit_released"] = False
    shoot = scene.addObject(name+"_physics",own,0)
    shoot.worldScale = [0.197,0.197,0.197]
    shoot["owner_ID"] = own.parent["ID"]
    shoot.mass = mass
    shoot.setLinearVelocity([-180,0,0], True)
    own.parent[name_inventory] -= 1

def aim_shoot_setup(own, scene, name, name_inventory, mass):
    own.parent["hit_released"] = False
    shoot = scene.addObject(name+"_physics",own,0)
    shoot.worldScale = [0.197,0.197,0.197]
    shoot["owner_ID"] = own.parent["ID"]
    shoot.mass = mass
    shoot.setLinearVelocity([-90,0,0], True)
    own.parent[name_inventory] -= 1

def shoot(cont):
    own = cont.owner
    if own.parent["hit_released"] and not own["AIM"]:
        scene = logic.getCurrentScene()
        if own.parent["weapon"] == 1:
            shoot_setup(own, scene, "snow_ball", "snow", 40000)
        elif own.parent["weapon"] == 2:
            shoot_setup(own, scene, "ice_cube", "ice", 60000)

def aim_shoot(cont):
    own = cont.owner
    if own.parent["hit_released"] and own["AIM"]:
        scene = logic.getCurrentScene()
        if own.parent["weapon"] == 1:
            aim_shoot_setup(own, scene, "snow_ball", "snow", 40000)
        elif own.parent["weapon"] == 2:
            aim_shoot_setup(own, scene, "ice_cube", "ice", 60000)

def hit(cont):
    own = cont.owner
    if own.parent["weapon"] == 0:
        hit = logic.getCurrentScene().addObject("hit",own,3)
        hit["owner_ID"] = own.parent["ID"]
        hit.setLinearVelocity([-45,0,0], True)
        own.parent["hit_released"] = False
