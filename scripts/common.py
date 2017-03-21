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
AI_MAX_DISTANCE = 100
AI_CLOSE_DISTANCE = 20
AI_MAX_COUNT = 15
AI_CLOSE_COUNT = 2
AI_SPAWN_MAX_DISTANCE = 100
AI_SPAWN_MIN_DISTANCE = 50

#TERRAIN
TERRAIN_GROUP_MAX_DISTANCE = 4000
TERRAIN_CHILD_GROUP_MAX_DISTANCE = 2000
TERRAIN_CHILD_CHILD_GROUP_MAX_DISTANCE = 1500
TERRAIN_MAX_DISTANCE = 1000
TERRAIN_PHYSICS_MAX_DISTANCE = 500
TERRAIN_BORDER_X = 2319
TERRAIN_BORDER_Y = 3487

#SPEED
DANGER_SPEED = 60
HIGH_DANGER_SPEED = 70
FATAL_SPEED = 90
DAMAGE_RATE = 0.05
HIGH_DAMAGE_RATE = 0.15
RIGID_SPEED = 1

scene = logic.getCurrentScene()

def getDistance(vector):
    return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2) + math.pow(vector[2], 2))
