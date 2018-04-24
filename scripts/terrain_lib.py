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

logic = common.logic
scene = common.scene
global_dict = logic.globalDict

def main(cont):
    own = cont.owner
    key = own["key"]
    terrain_name = own["lib_name"]
    terrain_lib = logic.expandPath("//" + global_dict["terrain_base_dir"] + terrain_name + ".blend")    
    if terrain_lib not in logic.LibList():
        logic.LibLoad(terrain_lib, "Scene")
        global_dict["terrain_dict"][key]["ready"] += 1
        print("Terrain library " + terrain_lib + " loaded")

    own.endObject()
