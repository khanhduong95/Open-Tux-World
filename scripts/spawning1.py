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
from scripts import common_functions as cf

AI_MAX_DISTANCE = 100
AI_CLOSE_DISTANCE = 20
AI_MAX_COUNT = 10
AI_CLOSE_COUNT = 2
TERRAIN_GROUP_MAX_DISTANCE = 2500
TERRAIN_CHILD_GROUP_MAX_DISTANCE = 1500
TERRAIN_MAX_DISTANCE = 500
TERRAIN_PHYSICS_MAX_DISTANCE = 250

logic = cf.logic
scene = logic.getCurrentScene()

def AI(cont):
    own = cont.owner
    AI_list = []
    AI_close_list = []
    for obj in scene.objects:
        distance = own.getDistanceTo(obj)
        if "AI" in obj and distance < AI_MAX_DISTANCE and obj not in AI_list:
            AI_list.append(obj)
            if distance < AI_CLOSE_DISTANCE:
                AI_close_list.append(obj)

    AI_count = len(AI_list)
    AI_close_count = len(AI_close_list)
    try:
        cube = scene.objects["Cube"]
        dist_cube = own.getDistanceTo(cube)
        dist_for_dir = own.getDistanceTo(cube.children["camera_track"].children["forward_dir"])
    except:
        return

    if 50 < dist_cube < 100 and dist_cube < dist_for_dir:
        if not own["spawn_AI"] and AI_count <= 5 and AI_close_count < 1:
            new_AI = scene.addObject("AI_penguin",own,0)
            own["spawn_AI"] = True
    elif 100 <= dist_cube < 200:
        if not own["spawn_AI"] and AI_count < 2 and AI_close_count < 1:
            scene.addObject("AI_penguin",own,0)
            own["spawn_AI"] = True
    else:
        own["spawn_AI"] = False

def player_terrain(cont):
    own = cont.owner
    terrain_list = logic.globalDict["terrain_list"]
    index_x = 0
    index_y = 0
    for index in range(12):
        index_pos = terrain_list[index][0]
        if cf.getDistance([index_pos[0] - own.worldPosition[0], index_pos[1] - own.worldPosition[1], index_pos[2] - own.worldPosition[2]]) < TERRAIN_GROUP_MAX_DISTANCE:
            for index_child in range(9):
                index_child_pos = terrain_list[index][1][index_child][0]
                if cf.getDistance([index_child_pos[0] - own.worldPosition[0], index_child_pos[1] - own.worldPosition[1], index_child_pos[2] - own.worldPosition[2]]) < TERRAIN_CHILD_GROUP_MAX_DISTANCE:
                    for index_child_child in range(9):
                        terrain_info = terrain_list[index][1][index_child][1][index_child_child]
                        index_child_child_pos = terrain_info[0]
                                                
                        terrain_name = "terrain"+"_"+str(index_x)+"_"+str(index_y)+"_"+str(index_child)+"_"+str(index_child_child)
                        try:
                            terrain = scene.objects[terrain_name]
                        except:
                            if (-TERRAIN_MAX_DISTANCE < index_child_child_pos[0] - own.worldPosition[0] < TERRAIN_MAX_DISTANCE) and (-TERRAIN_MAX_DISTANCE < index_child_child_pos[1] - own.worldPosition[2] < TERRAIN_MAX_DISTANCE):
                                terrain = scene.addObject(terrain_name, scene.objects["terrain_spawner"], 0)
                                terrain.worldPosition[0] = index_child_child_pos[0]
                                terrain.worldPosition[1] = index_child_child_pos[1]
                                terrain.worldPosition[2] = index_child_child_pos[2]#-50
                                print(terrain_name+" : "+str(terrain.worldScale))
                                      
                        try:
                            terrain_physics = scene.objects[terrain_name+"_physics"]
                        except:
                            if cf.getDistance([index_child_child_pos[0] - own.worldPosition[0], index_child_child_pos[1] - own.worldPosition[1], index_child_child_pos[2] - own.worldPosition[2]]) < TERRAIN_PHYSICS_MAX_DISTANCE:
                                terrain_physics = scene.addObject(terrain_name+"_physics", scene.objects["terrain_spawner"], 0)
                                terrain_physics.worldPosition[0] = index_child_child_pos[0]
                                terrain_physics.worldPosition[1] = index_child_child_pos[1]
                                terrain_physics.worldPosition[2] = index_child_child_pos[2]#-50

        if index_y >= 2:
            index_y = 0
            index_x += 1
        else:
            index_y += 1
