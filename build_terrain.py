import bpy
import bmesh
import pickle
import math
import os

ops = bpy.ops
wm = ops.wm

terrain_names = []
house_names = []

for file in os.listdir(bpy.path.abspath("//") + "terrains"):
    if file.endswith(".blend"):
        terrains = []
        houses = []
        blend = bpy.path.abspath("//") + "terrains/" + file
        with bpy.data.libraries.load(blend, relative=True) as (data_from, data_to):
            for name in data_from.objects:
                if name.startswith("terrain"):
                    terrains.append({'name': name})
                    if not name.endswith("_physics"):
                        terrain_names.append(name)
                elif name.startswith("house_spawner"):
                    houses.append({'name': name})
                    house_names.append(name) #add house to list with closest terrain piece and distance
                        
            wm.append(directory=blend + "/Object/", files=terrains)
            wm.append(directory=blend + "/Object/", files=houses)

obj_list = []
objects = bpy.data.objects
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers

#ops.object.mode_set(mode='OBJECT')

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

def get_distance(loc1, loc2):
    return math.sqrt(math.pow(loc1[0] - loc2[0], 2) + math.pow(loc1[1] - loc2[1], 2) + math.pow(loc1[2] - loc2[2], 2))
    
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
    terrain_loc_rot = {"location": [terrain.location[0], terrain.location[1], terrain.location[2]]}
    ops.object.select_all(action='DESELECT')
    cut_n = 0
    global obj_list
    if obj_length > 1:
        terrain_loc_rot["children"] = []
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
            terrain_loc_rot["children"].append(cut_terrain(sub_obj_name, sub_obj_length, sub_obj_width, obj_suffix))
            ########################
        ops.object.select_all(action='DESELECT')
        scene.objects.active = terrain
        terrain.select = True
        ops.object.delete()
        obj_list.remove(terrain)
    else:
        #add_logic_bricks(obj_name, obj_suffix)
        #add_physics(obj_name)
        terrain_loc_rot["name"] = obj_name+obj_suffix
        terrain_loc_rot["houses"] = []
        #terrain_loc_rot.append([terrain.rotation_euler[0], terrain.rotation_euler[1], terrain.rotation_euler[2]])
        #terrain_loc_rot.append([terrain.scale[0], terrain.scale[1], terrain.scale[2]])
    ops.object.select_all(action='DESELECT')
    return terrain_loc_rot

ops.object.select_all(action='DESELECT')

for terrain_name in terrain_names:
    terrain_list.extend(cut_terrain(terrain_name, 36, 36, "_physics")["children"])

for house_name in house_names:
    house_loc = objects[house_name].location
    closest_dist = -1
    closest1 = 0
    closest2 = 0
    closest3 = 0
    closest4 = 0
    for i in range(len(terrain_list)):
        terrain = terrain_list[i]
        terrain_loc = terrain["location"]
        dist = get_distance(terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest1 = i

    terrain_group = terrain_list[closest1]["children"]
    for i in range(len(terrain_group)):
        terrain = terrain_group[i]
        terrain_loc = terrain["location"]
        dist = get_distance(terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest2 = i

    terrain_group_child = terrain_group[closest2]["children"]
    for i in range(len(terrain_group_child)):
        terrain = terrain_group_child[i]
        terrain_loc = terrain["location"]
        dist = get_distance(terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest3 = i

    terrain_group_child_child = terrain_group_child[closest3]["children"]
    for i in range(len(terrain_group_child_child)):
        terrain = terrain_group_child[i]
        terrain_loc = terrain["location"]
        dist = get_distance(terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest4 = i

    terrain_list[closest1]["children"][closest2]["children"][closest3]["children"][closest4]["houses"].append(house_name)
            
pickle.dump(terrain_list, open(bpy.path.abspath("//")+"terrain_loc_rot.p", "wb"))

#cut_terrain("terrain", 216, 216, "_physics")

house = objects["house_image"]
sky = objects["Sky"]
select_layer(1)
smooth(sky)
select_layer(2)
smooth(house)

wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"terrain.blend")
wm.quit_blender()
