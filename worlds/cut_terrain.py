import bpy
import bmesh
import json
import math
import os

ops = bpy.ops
wm = ops.wm

terrain_names = []
house_names = []

obj_list = []
group_list = []
objects = bpy.data.objects
groups = bpy.data.groups
context = bpy.context
scene = context.scene
logic = ops.logic
layers = scene.layers
current_file = bpy.data.filepath
file_name = bpy.path.basename(current_file)

max_x = 0 
min_x = 0 
max_y = 0
min_y = 0
with open(os.path.join(bpy.path.abspath("//"), os.pardir, "terrain_config.json"), "r") as json_file:
    terrain_config = json.load(json_file)
    physics_distance = terrain_config["physics_distance"]
    image_distance = terrain_config["image_distance"]
    physics_max_neighbors = terrain_config["physics_max_neighbors"] + 1
    image_max_neighbors = terrain_config["image_max_neighbors"] + 1

for ob in objects:
    if ob not in obj_list:
        obj_list.append(ob)

for gr in groups:
    if gr not in group_list:
        group_list.append(gr)

for obj in objects:
    name = obj.name
    if name.startswith("terrain"):
        if not name.endswith("_physics"):
            terrain_names.append(name)
    elif name.startswith("house_spawner"):
        house_names.append(name) #add house to list with closest terrain piece and distance                        

terrain_list = {}

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

def get_distance(loc1, loc2):
    return math.sqrt(math.pow(loc1[0] - loc2[0], 2) + math.pow(loc1[1] - loc2[1], 2) + math.pow(loc1[2] - loc2[2], 2))

def map_physics_group(terrain_group):
    global terrain_list
    global max_x
    global min_x
    global max_y
    global min_y
    print("Mapping terrain group: "+terrain_group)
    select_layer(2)
    ops.object.group_instance_add(name=terrain_group, location=(0,0,0))
    new_group = objects[terrain_group]
    ops.object.origin_set(type='ORIGIN_GEOMETRY')
    terrain_loc = new_group.location

    keys = []
    for i in range(3):
        key = terrain_loc[i] // physics_distance
        neighbors = [str(key)]
        for j in range(1, physics_max_neighbors):
            neighbors.append(str(key + j))
            neighbors.append(str(key - j))
        keys.append(neighbors)

    for x in keys[0]:        
        for y in keys[1]:
            for z in keys[2]:
                if x+"_"+y+"_"+z not in terrain_list["physics"]:
                    terrain_list["physics"][x+"_"+y+"_"+z] = []
                if terrain_loc[0] < min_x:
                    min_x = terrain_loc[0]
                elif terrain_loc[0] > max_x:
                    max_x = terrain_loc[0]
                if terrain_loc[1] < min_y:
                    min_y = terrain_loc[1]
                elif terrain_loc[1] > max_y:
                    max_y = terrain_loc[1]
                terrain_list["physics"][x+"_"+y+"_"+z].append({"name": terrain_group, "location": [terrain_loc[0], terrain_loc[1], terrain_loc[2]], "houses": []})

    select_layer(1)
    ops.object.select_all(action='DESELECT')

def cut_terrain(obj_name, obj_suffix):
    print("Cutting terrain: "+obj_name+obj_suffix)
    
    terrain = objects[obj_name+obj_suffix]
    obj_length = int(math.sqrt(len(terrain.data.vertices))) - 1
    scene.objects.active = terrain
    terrain.select = True
    ops.object.origin_set(type='ORIGIN_GEOMETRY')    
    ops.object.select_all(action='DESELECT')
    global terrain_list
    global obj_list
    global group_list
    if obj_length > 5 and obj_length % 3 == 0:
        cut_n = 0
        range_square = 9
        for i in range(range_square):
            scene.objects.active = terrain
            terrain.select = True
            ops.object.mode_set(mode='EDIT')
            obj = context.object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            ops.mesh.select_all(action='DESELECT')
            ########################
            sub_obj_length = obj_length // 3
            range_length = range(sub_obj_length + 1)
            connected_faces = {}
            
            bm.verts.ensure_lookup_table()
            for m in range_length:
                for n in range_length:
                    vert = bm.verts[m + n*(obj_length + 1 - cut_n) + (cut_n if i < 6 and n == sub_obj_length else 0)]
                    for face in vert.link_faces:
                        face_index = str(face.index)
                        try:
                            connected_faces[face_index].add(vert.index)
                        except:
                            connected_faces[face_index] = set([vert.index])
                        if len(connected_faces[face_index]) > 3:
                            face.select = True
            bmesh.update_edit_mesh(me, True)
            bm.verts.ensure_lookup_table()
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
            cut_terrain(sub_obj_name, obj_suffix)
        ########################
    else:
        range_square = int(math.pow(obj_length, 2))
        terrain_group = obj_name+obj_suffix+"_group"
        ops.object.group_add()
        for gr in groups:
            if gr not in group_list:
                gr.name = terrain_group
                group_list.append(gr)
                map_physics_group(terrain_group)
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
            # try:
            bm.faces[0].select = True
            # except:
            #     wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), os.pardir, file_name))
            #     wm.quit_blender()
                
            bmesh.update_edit_mesh(me, True)
            bm.faces.ensure_lookup_table()                
            ########################
            bpy.ops.mesh.separate(type='SELECTED')
            ########################
            sub_obj_name = obj_name+"_"+str(i)
            ops.object.mode_set(mode='OBJECT')
            ops.object.select_all(action='DESELECT')
            for ob in objects:
                if ob not in obj_list and not ob.name.endswith(obj_suffix + "_group"):
                    ob.name = sub_obj_name+obj_suffix
                    obj_list.append(ob)
                    break
        ########################
    ops.object.select_all(action='DESELECT')
    scene.objects.active = terrain
    terrain.select = True
    ops.object.delete()
    obj_list.remove(terrain)    

ops.object.select_all(action='DESELECT')

select_layer(1)
terrain_list["image"] = {}
terrain_list["physics"] = {}
for terrain_name in terrain_names:
    terrain_image = objects[terrain_name]
    terrain_loc = terrain_image.location
    smooth(terrain_image)
    keys = []
    for i in range(2):
        key = terrain_loc[i] // image_distance
        neighbors = [str(key)]
        for j in range(1, image_max_neighbors):
            neighbors.append(str(key + j))
            neighbors.append(str(key - j))
        keys.append(neighbors)

    for x in keys[0]:        
        for y in keys[1]:
            if x+"_"+y not in terrain_list["image"]:
                terrain_list["image"][x+"_"+y] = []
            terrain_list["image"][x+"_"+y].append({"name": terrain_name, "location": [terrain_loc[0], terrain_loc[1], terrain_loc[2]]})
    
    cut_terrain(terrain_name, "_physics")

for house_name in house_names:
    house_loc = objects[house_name].location
    house_rot = objects[house_name].rotation_euler
    closest_dist = -1
    closest = 0
    x = str(house_loc[0] // physics_distance)
    y = str(house_loc[1] // physics_distance)
    z = str(house_loc[2] // physics_distance)

    nearest_terrains = terrain_list["physics"][x+"_"+y+"_"+z]
    for i in range(len(nearest_terrains)):
        nearest_terrain = nearest_terrains[i]
        nearest_terrain_loc = nearest_terrain["location"]
        dist = get_distance(nearest_terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest = i

    terrain_list["physics"][x+"_"+y+"_"+z][closest]["houses"].append({"location": [house_loc[0], house_loc[1], house_loc[2]], "rotation": [house_rot[0], house_rot[1], house_rot[2]]})

terrain_list["min_x"] = min_x
terrain_list["max_x"] = max_x
terrain_list["min_y"] = min_y
terrain_list["max_y"] = max_y
json.dump(terrain_list, open(os.path.join(bpy.path.abspath("//"), file_name[:-len(".blend")] + "_dict.json"), "w"))

select_layer(0)
wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), file_name))
wm.quit_blender()
