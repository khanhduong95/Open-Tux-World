#
#    Copyright (C) 2018 Dang Duong
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

logic = common.logic
scene = common.scene
global_dict = logic.globalDict

def main(cont):
    own = cont.owner
    terrain_name = own["terrain_name"]
    terrain_lib = logic.expandPath("//" + global_dict["terrain_base_dir"] + terrain_name + ".blend")
        
    if terrain_lib not in logic.LibList():
        dict_dir = global_dict["terrain_dict_dir"]
        with open(dict_dir + terrain_name + "_data.json", "r") as json_file:
            json_data = json.load(json_file)
            own.worldPosition = json_data["location"]
        
            logic.LibLoad(terrain_lib, "Scene")
            print("Terrain library " + terrain_lib + " loaded")
            print("Terrain " + terrain_name +" added")

            if own["physics"]:
                houses = json_data["houses"]
                for house_name in houses:
                    house_physics = scene.addObject("house_physics", scene.objects[house_name], 0)
                    house_physics.setParent(own, 0, 0)

    own.state = logic.KX_STATE3
