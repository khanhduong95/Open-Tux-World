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
from bge import logic
import math

#AI
# AI_MAX_DISTANCE = 100
# AI_CLOSE_DISTANCE = 50
AI_MAX_COUNT = 25
AI_NEW_SPAWN_MAX_COUNT = 5
AI_CLOSE_COUNT = 5
AI_SPAWN_MAX_DISTANCE = 200
AI_SPAWN_MIN_DISTANCE = 50

AI_ATTACK_MAX_DISTANCE = 200

AI_DIST_LOC_MAX = 300
AI_DIST_LOC_MIN = 150
AI_DIST_LOC_MAX_DEATH = 150
AI_DIST_LOC_MIN_DEATH = 40

#TERRAIN
TERRAIN_IMAGE_MAX_DISTANCE = 0
TERRAIN_PHYSICS_MAX_DISTANCE = 0
TERRAIN_IMAGE_MAX_NEIGHBORS = 0
TERRAIN_PHYSICS_MAX_NEIGHBORS = 0
TERRAIN_BORDER_MAX_X = 0
TERRAIN_BORDER_MIN_X = 0
TERRAIN_BORDER_MAX_Y = 0
TERRAIN_BORDER_MIN_Y = 0

#SPEED
DANGER_SPEED = 60
HIGH_DANGER_SPEED = 70
FATAL_SPEED = 90
DAMAGE_RATE = 0.05
HIGH_DAMAGE_RATE = 0.15
RIGID_SPEED = 2

#ITEM
ITEM_MAX_COUNT = 30
ITEM_COLLECT_EXPIRE = 1200
ITEM_MAX_DISTANCE = 150

scene = logic.getCurrentScene()

def getDistance(vector):
    return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2) + math.pow(vector[2], 2))
<<<<<<< HEAD
<<<<<<< HEAD

def steep_speed(own, steep_dir, aim, speed, forward, back, left, right):
    if aim:
        steep_dir.localPosition[0] = -speed if forward else (speed if back else 0)
        steep_dir.localPosition[1] = -speed if left else (speed if right else 0)
    else:
        steep_dir.localPosition[0] = -speed

    pos_x = steep_dir.worldPosition.x
    pos_y = steep_dir.worldPosition.y
    pos_z = steep_dir.worldPosition.z
    hitPos = steep_dir.rayCast([pos_x, pos_y, pos_z - 1], steep_dir, speed/2, "", 0, 0, 0)
    hitObj = hitPos[0]
    if hitObj and id(hitObj) != id(own):
        steep = hitPos[1][2] - pos_z
        if steep < 0:
            return steep
    return 0
=======
>>>>>>> 99a89667972cec7d9a2bfa8a3e814e7544eac66b
=======
>>>>>>> parent of fd4461f... add steep move
