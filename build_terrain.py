import bpy
import bmesh
import pickle

obj_list = []
objects = bpy.data.objects
ops = bpy.ops
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers

ops.object.mode_set(mode='OBJECT')

for ob in objects:
    if ob not in obj_list:
        obj_list.append(ob)

terrain_list = []

def select_layer(index):
    ops.object.select_all(action="DESELECT")
    layers[index] = True    
    for i in range(10):
        if i != index:
            layers[i] = False

def smooth(obj):
    ops.object.select_all(action="DESELECT")
    scene.objects.active = obj
    obj.select = True
    ops.object.shade_smooth()
    ops.object.select_all(action="DESELECT")

def cut_terrain(obj_name, obj_length, obj_width, obj_suffix):
    print("Cutting terrain: "+obj_name+obj_suffix)
    if obj_length >= obj_width:
        sub_obj_length = int(obj_length/3)
        sub_obj_width = int(obj_width/2)
    else:
        sub_obj_length = int(obj_length/2)
        sub_obj_width = int(obj_width/3)
    terrain = objects[obj_name+obj_suffix]
    scene.objects.active = terrain
    terrain.select = True
    ops.object.origin_set(type='ORIGIN_GEOMETRY')
    terrain_loc_rot = [[terrain.location[0], terrain.location[1], terrain.location[2]], []]
    ops.object.select_all(action='DESELECT')
    cut_n = 0
    global obj_list
    if obj_length > 1:
        for i in range(6):
            scene.objects.active = terrain
            terrain.select = True
            ops.object.mode_set(mode='EDIT')
            obj = context.object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            ops.mesh.select_all(action='DESELECT')
            ########################
            for m in range(sub_obj_width):
                for n in range(sub_obj_length):
                    bm.faces.ensure_lookup_table()
                    bm.faces[m + n*(obj_width - cut_n)].select = True
                    bmesh.update_edit_mesh(me, True)
                    bm.faces.ensure_lookup_table()
            ########################
            bpy.ops.mesh.separate(type='SELECTED')
            if cut_n < obj_width - sub_obj_width:
                cut_n += sub_obj_width
            else:
                cut_n = 0
            ########################
            sub_obj_name = obj_name+"_"+str(i)
            ops.object.mode_set(mode='OBJECT')
            ops.object.select_all(action='DESELECT')
            for ob in objects:
                if ob not in obj_list:
                    ob.name = sub_obj_name+obj_suffix
                    obj_list.append(ob)
                    break
            ########################
            terrain_loc_rot[1].append(cut_terrain(sub_obj_name, sub_obj_length, sub_obj_width, obj_suffix))
            ########################
        ops.object.select_all(action='DESELECT')
        scene.objects.active = terrain
        terrain.select = True
        ops.object.delete()
        obj_list.remove(terrain)
    else:
        #add_logic_bricks(obj_name, obj_suffix)
        #add_physics(obj_name)
        terrain_loc_rot.append([terrain.rotation_euler[0], terrain.rotation_euler[1], terrain.rotation_euler[2]])
        terrain_loc_rot.append([terrain.scale[0], terrain.scale[1], terrain.scale[2]])
    ops.object.select_all(action='DESELECT')
    return terrain_loc_rot

ops.object.select_all(action='DESELECT')

terrain_list = cut_terrain("terrain", 36, 36, "_physics")
pickle.dump(terrain_list, open(bpy.path.abspath("//")+"terrain_loc_rot.p", "wb"))

#cut_terrain("terrain", 216, 216, "_physics")

house = objects["house_image"]
sky = objects["Sky"]
select_layer(1)
smooth(sky)
select_layer(2)
smooth(house)

ops.wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"terrain.blend")
ops.wm.quit_blender()
