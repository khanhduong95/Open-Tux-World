import bpy
import bmesh
import json
import math
import os
import errno

ops = bpy.ops
wm = ops.wm

terrain_names = []
terrain_physics_names = []
house_names = []

obj_list = []
physics_parent_list = []
objects = bpy.data.objects
context = bpy.context
scene = context.scene
logic = ops.logic
current_file = bpy.data.filepath
file_name = bpy.path.basename(current_file)
file_name_no_blend = file_name[:-len(".blend")]

terrain_image_list = []

max_x = 0 
min_x = 0 
max_y = 0
min_y = 0
with open(os.path.join(bpy.path.abspath("//"), os.pardir, "terrain_config.json"), "r") as json_file:
    terrain_config = json.load(json_file)
    physics_distance = terrain_config["physics_distance"]
    image_distance = terrain_config["image_distance"]
    physics_max_neighbors = terrain_config["physics_max_neighbors"]
    image_max_neighbors = terrain_config["image_max_neighbors"]

for ob in objects:
    if ob not in obj_list:
        obj_list.append(ob)

for obj in objects:
    name = obj.name
    if name.startswith("terrain"):
        if name.endswith("_physics"):
            terrain_physics_names.append(name)
        else:
            terrain_names.append(name)
            
    elif name.startswith("house_spawner"):
        house_names.append(name) #add house to list with closest terrain piece and distance                        

terrain_list = {"image": {}, "physics": {}}
terrain_data = {}

def smooth(obj):
    ops.object.select_all(action="DESELECT")
    scene.objects.active = obj
    obj.select = True
    ops.object.shade_smooth()
    ops.object.select_all(action="DESELECT")

def get_distance(loc1, loc2):
    return math.sqrt(math.pow(loc1[0] - loc2[0], 2) + math.pow(loc1[1] - loc2[1], 2) + math.pow(loc1[2] - loc2[2], 2))

def map_image(terrain_name):
    print("Mapping terrain image: "+terrain_name)
    terrain_image = objects[terrain_name]
    scene.objects.active = terrain_image
    terrain_image.select = True
    ops.object.origin_set(type='ORIGIN_GEOMETRY')    
    ops.object.select_all(action='DESELECT')
    terrain_loc = terrain_image.location

    key_x = int(terrain_loc[0] / image_distance)
    key_y = int(terrain_loc[1] / image_distance)
    key = str(key_x) + "_" + str(key_y)
    if key not in terrain_list["image"]:
        terrain_list["image"][key] = []
    terrain_list["image"][key].append(terrain_name)
    terrain_data[terrain_name] = {"location": [terrain_loc[0], terrain_loc[1], terrain_loc[2]]}
    if terrain_name != file_name_no_blend:
        terrain_image_list.append(terrain_name)

    ops.object.select_all(action='DESELECT')

def map_physics_parent(terrain_parent, terrain):
    global max_x
    global min_x
    global max_y
    global min_y
    print("Mapping terrain parent: "+terrain_parent)
    # ops.object.origin_set(type='ORIGIN_GEOMETRY')
    terrain_loc = terrain.location
    ops.object.empty_add(type="PLAIN_AXES", location=(terrain_loc[0], terrain_loc[1], terrain_loc[2]))
    empty = objects["Empty"]
    empty.name = terrain_parent
    ops.object.select_all(action='DESELECT')
    scene.objects.active = terrain
    terrain.select = True    
    scene.objects.active = empty
    empty.select = True
    ops.object.parent_set(type='OBJECT')
    physics_parent_list.append(terrain_parent)

    key_x = int(terrain_loc[0] / physics_distance)
    key_y = int(terrain_loc[1] / physics_distance)
    key_z = int(terrain_loc[2] / physics_distance)
    key = str(key_x) + "_" + str(key_y) + "_" + str(key_z)
    if key not in terrain_list["physics"]:
        terrain_list["physics"][key] = []
    if terrain_loc[0] < min_x:
        min_x = terrain_loc[0]
    elif terrain_loc[0] > max_x:
        max_x = terrain_loc[0]
    if terrain_loc[1] < min_y:
        min_y = terrain_loc[1]
    elif terrain_loc[1] > max_y:
        max_y = terrain_loc[1]
    terrain_list["physics"][key].append(terrain_parent)
    terrain_data[terrain_parent] = {"location": [terrain_loc[0], terrain_loc[1], terrain_loc[2]], "houses": []}

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
    if obj_length > 8 and obj_length % 3 == 0:
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
                if ob not in obj_list and not ob.name.endswith(obj_suffix + "_parent"):
                    ob.name = sub_obj_name+obj_suffix
                    obj_list.append(ob)
                    break
            ########################
            if obj_suffix == "_physics":
                cut_terrain(sub_obj_name, obj_suffix)
            else:
                map_image(sub_obj_name)
        ########################
    elif obj_suffix == "_physics":
        range_square = int(math.pow(obj_length, 2))
        terrain_parent = obj_name+obj_suffix+"_parent"
        map_physics_parent(terrain_parent, terrain)
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
                if ob not in obj_list and not ob.name.endswith(obj_suffix + "_parent"):
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

for terrain_name in terrain_names:
    terrain_image = objects[terrain_name]
    smooth(terrain_image)
    map_image(terrain_name)
    # cut_terrain(terrain_name, "")

for terrain_name in terrain_physics_names:
    cut_terrain(terrain_name[:-len("_physics")], "_physics")

for house_name in house_names:
    house_loc = objects[house_name].location
    house_rot = objects[house_name].rotation_euler
    closest_dist = -1
    key_x = int(house_loc[0] / physics_distance)
    key_y = int(house_loc[1] / physics_distance)
    key_z = int(house_loc[2] / physics_distance)
    nearest_terrains = []
    for x in range(key_x - physics_max_neighbors, key_x + physics_max_neighbors + 1):
        for y in range(key_y - physics_max_neighbors, key_y + physics_max_neighbors + 1):
            for z in range(key_z - physics_max_neighbors, key_z + physics_max_neighbors + 1):
                key = str(x) + "_" + str(y) + "_" + str(z)
                if key in terrain_list["physics"]:
                    nearest_terrains.extend(terrain_list["physics"][key])                    
    for nearest_terrain in nearest_terrains:
        nearest_terrain_loc = terrain_data[nearest_terrain]["location"]
        dist = get_distance(nearest_terrain_loc, house_loc)
        if closest_dist < 0 or dist < closest_dist:
            closest_dist = dist
            closest = nearest_terrain
    
    terrain_data[closest]["houses"].append(house_name)

dict_dir = os.path.join(bpy.path.abspath("//"), "dictionaries", "")
json.dump({"min_x": min_x, "max_x": max_x, "min_y": min_y, "max_y": max_y}, open(dict_dir + file_name_no_blend + "_borders.json", "w"))

for terrain_type in ["image", "physics"]:
    for k, v in terrain_list[terrain_type].items():
        loc_dir = os.path.join(dict_dir, terrain_type, k, "")
        try:
            os.makedirs(loc_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        json.dump(v, open(os.path.join(loc_dir, file_name_no_blend + ".json"), "w"))

for k, v in terrain_data.items():
    json.dump(v, open(os.path.join(dict_dir, k + "_data.json"), "w"))    

# json.dump(terrain_list, open(os.path.join(bpy.path.abspath("//"), "dictionaries", file_name[:-len(".blend")] + "_dict.json"), "w"))

wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), file_name))

ops.object.select_all(action='DESELECT')

for physics_parent_name in physics_parent_list:
    ops = bpy.ops
    wm = ops.wm
    objects = bpy.data.objects
    context = bpy.context
    scene = context.scene
    for obj in objects:
        if obj.name != physics_parent_name and (not obj.parent or obj.parent.name != physics_parent_name):
            scene.objects.active = obj
            obj.select = True

    ops.object.delete(use_global = True)
    wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), physics_parent_name + ".blend"), copy = True)
    wm.revert_mainfile()        

# for image_name in terrain_image_list:
#     ops = bpy.ops
#     wm = ops.wm
#     objects = bpy.data.objects
#     context = bpy.context
#     scene = context.scene
#     for obj in objects:
#         if obj.name != image_name and (not obj.parent or obj.parent.name != image_name):
#             scene.objects.active = obj
#             obj.select = True

#     ops.object.delete(use_global = True)
#     wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), image_name + ".blend"), copy = True)
#     wm.revert_mainfile()        

ops = bpy.ops
wm = ops.wm
objects = bpy.data.objects
context = bpy.context
scene = context.scene
for obj in objects:
    if obj.name != file_name_no_blend and (not obj.parent or obj.parent.name != file_name_no_blend):
        scene.objects.active = obj
        obj.select = True

ops.object.delete(use_global = True)
wm.save_as_mainfile(filepath = os.path.join(bpy.path.abspath("//"), file_name))
wm.quit_blender()
