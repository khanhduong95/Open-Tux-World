import bpy
import platform

ops = bpy.ops
wm = ops.wm

context = bpy.context
scene = context.scene
layers = scene.layers

# ops.object.make_local(type="ALL")
# bpy.data.scenes["Scene"].game_settings.show_physics_visualization = True
bpy.data.scenes["Scene"].game_settings.show_fullscreen = True

def select_layer(index):
    ops.object.select_all(action="DESELECT")
    layers[index] = True    
    for i in range(10):
        if i != index:
            layers[i] = False

blend = bpy.path.abspath("//")+"terrain.blend"
with bpy.data.libraries.load(blend, relative=True) as (data_from, data_to):
    terrains = []
    terrain_physics = []
    for name in data_from.objects:
        if name.startswith("terrain") and name != "terrain_loc":
            if name.endswith("_physics_group"):
                terrain_physics.append({'name': name})
            elif not name.endswith("_physics"):
                terrains.append({'name': name})
        elif name.startswith("house_spawner"):
            terrains.append({'name': name})
    select_layer(5)
    wm.link(directory=blend + "/Object/", files=terrains)
    wm.link(directory=blend + "/Object/", files=terrain_physics)
    select_layer(0)

os_name = platform.system()
if os_name == "Windows":
    exe_extension = ".exe"
elif os_name == "MacOS":
    exe_extension = ".app"
else:
    exe_extension = ""
            
wm.addon_enable(module="game_engine_save_as_runtime")
wm.save_as_runtime(filepath=bpy.path.abspath("//")+"otw"+exe_extension)
# wm.save_as_mainfile(filepath=bpy.path.abspath("//")+"otw.blend")
wm.quit_blender()
