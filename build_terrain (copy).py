import bpy
import bmesh
import json
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
group_list = []
objects = bpy.data.objects
groups = bpy.data.groups
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers

#ops.object.mode_set(mode='OBJECT')

for ob in objects:
    if ob not in obj_list:
        obj_list.append(ob)

for gr in groups:
    if gr not in group_list:
        group_list.append(gr)

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
    
def cut_terrain(obj_name, obj_suffix):
    print("Cutting terrain: "+obj_name+obj_suffix)
    
    terrain = objects[obj_name+obj_suffix]
    obj_length = int(math.sqrt(len(terrain.data.vertices))) - 1
    scene.objects.active = terrain
    terrain.select = True
    ops.object.origin_set(type='ORIGIN_GEOMETRY')
    terrain_loc_rot = {"location": [terrain.location[0], terrain.location[1], terrain.location[2]]}
    ops.object.select_all(action='DESELECT')
    cut_n = 0
    global obj_list
    global group_list
    if obj_length > 5 and obj_length % 3 == 0:
        range_square = 9
        terrain_loc_rot["children"] = []        
        for i in range(range_square):
            scene.objects.active = terrain
            terrain.select = True
            ops.object.mode_set(mode='EDIT')
            obj = context.object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            ops.mesh.select_all(action='DESELECT')
            ########################
            sub_obj_length = int(obj_length/3)
            range_length = range(sub_obj_length)                
            for m in range_length:
                for n in range_length:
                    bm.faces.ensure_lookup_table()
                    bm.faces[m + n*(obj_length - cut_n)].select = True
                    bmesh.update_edit_mesh(me, True)
                    bm.faces.ensure_lookup_table()
            if cut_n < obj_length - sub_obj_length:
                cut_n += sub_obj_length
            else:
                cut_n = 0
            ########################
            bpy.ops.mesh.separate(type='SELECTED')
            ########################
            sub_obj_name = obj_name+"_"+str(i)
            ops.object.mode_set(mode='OBJECT')
            ops.object.select_all(action='DESELECT')
            for ob in objects:
                if ob not in obj_list and not ob.name.endswith("_physics_group"):
                    ob.name = sub_obj_name+obj_suffix
                    obj_list.append(ob)
                    break
            ########################
            terrain_loc_rot["children"].append(cut_terrain(sub_obj_name, obj_suffix))
        ########################
    else:
        range_square = int(math.pow(obj_length, 2))
        terrain_group = obj_name+obj_suffix+"_group"
        ops.object.group_add()
        terrain_loc_rot["name"] = terrain_group
        terrain_loc_rot["houses"] = []                
        for gr in groups:
            if gr not in group_list:
                gr.name = terrain_group
                group_list.append(gr)
                select_layer(3)
                ops.object.group_instance_add(name=terrain_group, location=(0,0,0))
                new_group = objects[terrain_group]
                ops.object.origin_set(type='ORIGIN_GEOMETRY')
                terrain_loc_rot["location"] = [new_group.location[0], new_group.location[1], new_group.location[2]]
                select_layer(0)
                ops.object.select_all(action='DESELECT')
                break            
        ########################
        for i in range(range_square):
            scene.objects.active = terrain
            terrain.select = True
            ops.object.mode_set(mode='EDIT')
            obj = context.object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            ops.mesh.select_all(action='DESELECT')
            ########################
            bm.faces.ensure_lookup_table()
            bm.faces[0].select = True
            bmesh.update_edit_mesh(me, True)
            bm.faces.ensure_lookup_table()                
            ########################
            bpy.ops.mesh.separate(type='SELECTED')
            ########################
            sub_obj_name = obj_name+"_"+str(i)
            ops.object.mode_set(mode='OBJECT')
            ops.object.select_all(action='DESELECT')
            for ob in objects:
                if ob not in obj_list and not ob.name.endswith("_physics_group"):
                    ob.name = sub_obj_name+obj_suffix
                    obj_list.append(ob)
                    break
        ########################
    ops.object.select_all(action='DESELECT')
    scene.objects.active = terrain
    terrain.select = True
    ops.object.delete()
    obj_list.remove(terrain)    
    return terrain_loc_rot

ops.object.select_all(action='DESELECT')

for terrain_name in terrain_names:
    terrain_list.extend(cut_terrain(terrain_name, "_physics")["children"])

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

    # terrain_group_child = terrain_group[closest2]["children"]
    # for i in range(len(terrain_group_child)):
    #     terrain = terrain_group_child[i]
    #     terrain_loc = terrain["location"]
    #     dist = get_distance(terrain_loc, house_loc)
    #     if closest_dist < 0 or dist < closest_dist:
    #         closest_dist = dist
    #         closest3 = i

    # terrain_group_child_child = terrain_group_child[closest3]["children"]
    # for i in range(len(terrain_group_child_child)):
    #     terrain = terrain_group_child[i]
    #     terrain_loc = terrain["location"]
    #     dist = get_distance(terrain_loc, house_loc)
    #     if closest_dist < 0 or dist < closest_dist:
    #         closest_dist = dist
    #         closest4 = i

    terrain_list[closest1]["children"][closest2]["houses"].append(house_name)
            
json.dump(terrain_list, open(bpy.path.abspath("//")+"terrain_loc_rot.json", "w"))

#cut_terrain("terrain", 216, 216, "_physics")

house = objects["house_image"]
sky = objects["Sky"]
select_layer(1)
smooth(sky)
select_layer(2)
smooth(house)        

wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"terrain.blend")
wm.quit_blender()
