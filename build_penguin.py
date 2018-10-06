import bpy

objects = bpy.data.objects
ops = bpy.ops
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers

player = objects["body"]
AI = objects["AI_body"]

def smooth(obj):
    ops.object.select_all(action="DESELECT")
    scene.objects.active = obj
    obj.select = True
    ops.object.modifier_apply(apply_as="DATA", modifier="Mirror")
    ops.object.shade_smooth()
    ops.object.select_all(action="DESELECT")

def select_layer(index):
    ops.object.select_all(action="DESELECT")
    layers[index] = True    
    for i in range(10):
        if i != index:
            layers[i] = False

select_layer(1)
smooth(player)

select_layer(3)
smooth(AI)

ops.wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"penguin.blend")
ops.wm.quit_blender()
