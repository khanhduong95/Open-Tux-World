import bpy
import os
import json

ops = bpy.ops
wm = ops.wm

obj_list = []

def select_layer(index, ops):
    ops.object.select_all(action="DESELECT")
    layers[index] = True    
    for i in range(len(layers)):
        if i != index:
            layers[i] = False

for obj in bpy.data.objects:
    obj_name = obj.name
    if obj_name.startswith("terrain") and not obj_name.endswith("_physics"):
        obj_list.append(obj_name)

build_dir = bpy.path.abspath("//") + "build"
if not os.path.exists(build_dir):
    os.makedirs(build_dir)
    
for obj_name in obj_list:
    ops = bpy.ops
    wm = ops.wm    
    objects = bpy.data.objects
    context = bpy.context
    scene = context.scene
    layers = scene.layers
    select_layer(1, ops)
    ops.object.select_all(action='DESELECT')
    print("Separating " + obj_name)
    for obj in objects:
        if obj.name != obj_name and obj.name != obj_name + "_physics" and (not obj.parent or obj.parent.name != obj_name):
            scene.objects.active = obj
            obj.select = True
    ops.object.delete(use_global = True)
    wm.save_as_mainfile(filepath = os.path.join(build_dir, obj_name + ".blend"), copy = True)
    wm.revert_mainfile()
    
wm.quit_blender()
