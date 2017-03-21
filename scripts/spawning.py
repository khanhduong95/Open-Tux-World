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
terrain_spawner = scene.objects["terrain_spawner"]

def compare_distance(own, terrain_loc, dist_const):
    return common.getDistance([terrain_loc[0] - own.worldPosition[0], terrain_loc[1] - own.worldPosition[1], terrain_loc[2] - own.worldPosition[2]]) < dist_const

def check_AI(terrain):
    AI_list = logic.globalDict["AI_list"]
    if len(AI_list) <= common.AI_MAX_COUNT:
        close_AI = 0
        for AI_id in AI_list:
            try:
                AI = scene.objects.from_id(AI_id)
                if AI.getDistanceTo(terrain) <= common.AI_CLOSE_DISTANCE:
                    close_AI += 1
            except:
                logic.globalDict["AI_list"].remove(AI_id)

        if close_AI < common.AI_CLOSE_COUNT:
            try:
                player = scene.objects["Cube"]
                dist_player = terrain.getDistanceTo(player)
                dist_for_dir = terrain.getDistanceTo(player.children["camera_track"].children["forward_dir"])
                if common.AI_SPAWN_MIN_DISTANCE < dist_player < common.AI_SPAWN_MAX_DISTANCE and dist_player < dist_for_dir:
                    terrain_spawner.worldPosition = terrain.worldPosition
                    terrain_spawner.worldPosition[2] += 5
                    new_AI = scene.addObject("AI_penguin", terrain_spawner, 0)
                    AI_Cube = new_AI.groupMembers["AI_Cube"]
                    logic.globalDict["AI_list"].append(id(AI_Cube))
                    
            except:
                return


def player_terrain(cont):
    own = cont.owner
    terrain_list = logic.globalDict["terrain_list"]
    for index in range(6):
        if compare_distance(own, terrain_list[index][0], common.TERRAIN_GROUP_MAX_DISTANCE):
            for index_child in range(6):
                if compare_distance(own, terrain_list[index][1][index_child][0], common.TERRAIN_CHILD_GROUP_MAX_DISTANCE):
                    for index_child_child in range(6):
                        if compare_distance(own, terrain_list[index][1][index_child][1][index_child_child][0], common.TERRAIN_CHILD_CHILD_GROUP_MAX_DISTANCE):
                            for index_child_child_child in range(6):
                                index_child_child_child_pos = terrain_list[index][1][index_child][1][index_child_child][1][index_child_child_child][0]
                                terrain_name = "terrain_"+str(index)+"_"+str(index_child)+"_"+str(index_child_child)+"_"+str(index_child_child_child)
                                try:
                                    terrain_physics = scene.objects[terrain_name+"_physics"]
                                    check_AI(terrain_physics)
                                except:
                                    if compare_distance(own, index_child_child_child_pos, common.TERRAIN_PHYSICS_MAX_DISTANCE):
                                        terrain_spawner.worldPosition = index_child_child_child_pos
                                        scene.addObject(terrain_name+"_physics", terrain_spawner, 0)
