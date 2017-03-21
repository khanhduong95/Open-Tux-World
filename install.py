import bpy
import platform

ops = bpy.ops
wm = ops.wm

ops.object.make_local(type="ALL")
#bpy.data.scenes["Scene"].game_settings.show_physics_visualization = True

os_name = platform.system()
if os_name == "Windows":
    exe_extension = ".exe"
elif os_name == "MacOS":
    exe_extension = ".app"
else:
    exe_extension = ""
            
wm.addon_enable(module="game_engine_save_as_runtime")
wm.save_as_runtime(filepath=bpy.path.abspath("//")+"game"+exe_extension)
wm.quit_blender()
