import bpy

ops = bpy.ops
wm = ops.wm

objects = bpy.data.objects
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers

def select_layer(index):
    ops.object.select_all(action="DESELECT")
    layers[index] = True
    for i in range(len(layers)):
        if i != index:
            layers[i] = False

def smooth(obj):
    ops.object.select_all(action="DESELECT")
    scene.objects.active = obj
    obj.select = True
    ops.object.shade_smooth()
    ops.object.select_all(action="DESELECT")

house = objects["house_image"]
sky = objects["Sky"]
select_layer(1)
smooth(sky)
select_layer(2)
smooth(house)

wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"terrain.blend")
wm.quit_blender()
