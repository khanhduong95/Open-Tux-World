import bpy
import platform

os_name = platform.system()
if os_name == "Windows":
    exe_extension = ".exe"
elif os_name == "MacOS":
    exe_extension = ".app"
else:
    exe_extension = ""
            
bpy.ops.wm.addon_enable(module="game_engine_save_as_runtime")
bpy.ops.wm.save_as_runtime(filepath=bpy.path.abspath("//")+"game"+exe_extension)
bpy.ops.wm.quit_blender()
