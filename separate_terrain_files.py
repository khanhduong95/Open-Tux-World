import bpy
import os
import math

ops = bpy.ops
wm = ops.wm
objects = bpy.data.objects
context = bpy.context
scene = context.scene

build_dir = bpy.path.abspath("//") + "build"
obj_list = []

for obj in objects:
    obj_name = obj.name
    if obj_name.startswith("terrain") and not obj_name.endswith("_physics"):
        obj_list.append(obj_name)

if not os.path.exists(build_dir):
    # os.makedirs(build_dir)
    os.makedirs(os.path.join(build_dir, "dictionaries"))
    
for obj_name in obj_list:
    ops = bpy.ops
    wm = ops.wm    
    objects = bpy.data.objects
    file_name = obj_name
    obj_length = int(math.sqrt(len(objects[obj_name].data.vertices))) - 1
    # if obj_length > 8 and obj_length % 3 == 0:
    #     file_name += "_0"
    context = bpy.context
    scene = context.scene
    ops.object.select_all(action='DESELECT')
    print("Separating " + obj_name)
    for obj in objects:
        if obj.name != obj_name and obj.name != obj_name + "_physics" and (not obj.parent or obj.parent.name != obj_name):
            scene.objects.active = obj
            obj.select = True
    ops.object.delete(use_global = True)
    wm.save_as_mainfile(filepath = os.path.join(build_dir, file_name + ".blend"), copy = True)
    wm.revert_mainfile()
    
wm.quit_blender()
