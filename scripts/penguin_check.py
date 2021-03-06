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
    parent = own.parent

    for player_id in global_dict["player_list"]:
        try:
            player = scene.objects.from_id(player_id)
            if not player["player"]:
                global_dict["player_list"].remove(player_id)
                player.groupObject.endObject()
                print("penguin_check.py Player " + str(player_id) + " removed")
                
        except:
            global_dict["player_list"].remove(player_id)

    for AI_id in global_dict["AI_list"]:
        try:
            AI = scene.objects.from_id(AI_id)
            if not AI["AI"]:
                global_dict["AI_list"].remove(AI_id)
                AI.groupObject.endObject()
                print("penguin_check.py AI " + str(AI_id) + " removed")
                
        except:
            global_dict["AI_list"].remove(player_id)

