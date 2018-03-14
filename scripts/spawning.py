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

def close_distance(own_pos, terrain_loc, dist_const):
    return common.getDistance([terrain_loc[0] - own_pos[0], terrain_loc[1] - own_pos[1], terrain_loc[2] - own_pos[2]]) < dist_const

def spawn_AI(own, terrain):
    AI_count = len(logic.globalDict["AI_list"])

    if AI_count <= common.AI_MAX_COUNT:
        dist_player = terrain.getDistanceTo(own)
        dist_cam = terrain.getDistanceTo(own.parent.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"])
        if common.AI_SPAWN_MIN_DISTANCE < dist_player < common.AI_SPAWN_MAX_DISTANCE and dist_player > dist_cam:
            terrain_spawner.worldPosition = terrain.worldPosition
            terrain_spawner.worldPosition[2] += 5
            AI = scene.addObject("AI_penguin", terrain_spawner, 0).groupMembers["AI_Cube"]
            vec = AI.worldPosition - own.worldPosition
            AI.alignAxisToVect([vec.x, vec.y, 0], 0, 1)#point to player
        
def main(cont):
    own = cont.owner
    own_pos = own.worldPosition
    for terrain in logic.globalDict["terrain_list"]:
        if close_distance(own_pos, terrain["location"], common.TERRAIN_GROUP_MAX_DISTANCE):
            for terrain_child in terrain["children"]:
                if close_distance(own_pos, terrain_child["location"], common.TERRAIN_CHILD_GROUP_MAX_DISTANCE):
                    for terrain_child_child in terrain_child["children"]:
                        if close_distance(own_pos, terrain_child_child["location"], common.TERRAIN_CHILD_CHILD_GROUP_MAX_DISTANCE):
                            for terrain_child_child_child in terrain_child_child["children"]:
                                index_child_child_child_pos = terrain_child_child_child["location"]
                                terrain_name = terrain_child_child_child["name"]
                                try:
                                    terrain_physics = scene.objects[terrain_name]
                                    for house_name in terrain_child_child_child["houses"]:
                                        house = scene.objects[house_name]
                                        try:
                                            house_physics = terrain_physics.children["house_physics"]
                                        except:
                                            house_physics = scene.addObject("house_physics", house, 0)
                                            house_physics.setParent(terrain_physics, 0, 0)                                            
                                            
                                    spawn_AI(own, terrain_physics)

                                except:
                                    if close_distance(own_pos, index_child_child_child_pos, common.TERRAIN_PHYSICS_MAX_DISTANCE):
                                        terrain_spawner.worldPosition = index_child_child_child_pos
                                        scene.addObject(terrain_name, terrain_spawner, 0)





