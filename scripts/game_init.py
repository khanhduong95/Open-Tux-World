#
#    Copyright (C) 2016 Dang Duong
#
#    This file is part of Open Tux World.
#
#    Open Tux World is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Open Tux World is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Open Tux World.  If not, see <http://www.gnu.org/licenses/>.
#
from scripts import common
import json
import os

logic = common.logic
scene = common.scene
global_dict = logic.globalDict

def otw_main(cont):
    for file in os.listdir("levels"):
        if not file.endswith(".py"):
            global_dict["terrain_base_dir"] = "levels/" + file + "/"
            cont.activate(cont.actuators["Game"])
            break

def main():
    base_dir = logic.globalDict["terrain_base_dir"]

    with open(base_dir + "terrain_dict.json", "r") as json_file:
        global_dict["terrain_dict"] = json.load(json_file)
    with open(base_dir + "terrain_config.json", "r") as json_file:
        terrain_max_distance = json.load(json_file)
        common.TERRAIN_IMAGE_MAX_DISTANCE = terrain_max_distance["image_distance"]
        common.TERRAIN_PHYSICS_MAX_DISTANCE = terrain_max_distance["physics_distance"]
        logic.LibLoad("//" + base_dir + "terrain_data.blend", "Scene")
    print("Terrain folder " + base_dir + " loaded")
        
    global_dict["terrain_physics_list"] = {}        
    global_dict["terrain_image_list"] = {}        
    global_dict["player_list"] = []        
    global_dict["AI_list"] = []
    scene.objects["player_spawn_point"]["init"] = True

    print("Game started")
