from bge import logic

def change_item(own, new, current):
    scene = logic.getCurrentScene()
    if current == 1:
        own.children["snow_ball"].endObject()
    elif current == 2:
        own.children["ice_cube"].endObject()
    if new == 1:
        snow = scene.addObject("snow_ball",own,0)
        snow.setParent(own,0,1)
        snow.worldScale = [0.197,0.197,0.197]
    elif new == 2:
        ice = scene.addObject("ice_cube",own,0)
        ice.setParent(own,0,1)
        ice.worldScale = [0.197,0.197,0.197]

def main(cont):
    own = cont.owner
    new = own.parent.parent["item"] #new item
    current = own["current"] #current item
    if own.parent.parent["death"]:
        change_item(own, 0, current)
        own.state = logic.KX_STATE2
    elif new != current:
        change_item(own, new, current)
    own["current"] = new


