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
    for file in os.listdir("worlds"):
        if not file.endswith(".py") and not file.endswith(".sh"):
            base_dir = os.path.join("worlds", file, "build", "")
            global_dict["terrain_base_dir"] = base_dir
            global_dict["terrain_dict_dir"] = os.path.join(base_dir, "dictionaries", "")
            cont.activate(cont.actuators["Game"])
            break

def main():
    base_dir = global_dict["terrain_base_dir"]
    dict_dir = global_dict["terrain_dict_dir"]

    with open(os.path.join(base_dir, os.pardir, "terrain_config.json"), "r") as json_file:
        terrain_config = json.load(json_file)
        common.TERRAIN_IMAGE_MAX_DISTANCE = terrain_config["image_distance"]
        common.TERRAIN_PHYSICS_MAX_DISTANCE = terrain_config["physics_distance"]
        common.TERRAIN_IMAGE_MAX_NEIGHBORS = terrain_config["image_max_neighbors"]
        common.TERRAIN_PHYSICS_MAX_NEIGHBORS = terrain_config["physics_max_neighbors"]
        
    for file in os.listdir(dict_dir):
        if file.endswith("_borders.json"):
            with open(dict_dir + file, "r") as json_file:
                json_data = json.load(json_file)
                if json_data["max_x"] > common.TERRAIN_BORDER_MAX_X:
                    common.TERRAIN_BORDER_MAX_X = json_data["max_x"]
                if json_data["min_x"] < common.TERRAIN_BORDER_MIN_X:
                    common.TERRAIN_BORDER_MIN_X = json_data["min_x"]
                if json_data["max_y"] > common.TERRAIN_BORDER_MAX_Y:
                    common.TERRAIN_BORDER_MAX_Y = json_data["max_y"]
                if json_data["min_y"] < common.TERRAIN_BORDER_MIN_Y:
                    common.TERRAIN_BORDER_MIN_Y = json_data["min_y"]

    print("game_init.py Terrain folder " + base_dir + " loaded")
        
    global_dict["terrain_image_dict"] = set()
    global_dict["terrain_physics_dict"] = {}
    global_dict["active_terrain_list"] = set()
    global_dict["terrain_image_player_list"] = {}
    global_dict["terrain_physics_player_list"] = {}
    global_dict["player_list"] = []
    global_dict["AI_list"] = []

    scene.objects["player_spawn_point"]["init"] = True

    print("game_init.py Game started")
