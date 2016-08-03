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
from random import randint
import math

def shoot_setup(own, scene, name, name_inventory, mass):
    own.parent["hit_released"] = False
    shoot = scene.addObject(name+"_physics",own,0)
    shoot.worldScale = [0.197,0.197,0.197]
    shoot["owner_ID"] = id(own.parent)
    shoot.mass = mass
    shoot.setLinearVelocity([-90,0,0], True)
    own.parent[name_inventory] -= 1

def target_aim(cont):
    own = cont.owner
    if own["AIM"]:
        target = own.parent.children["camera_track"].children["camera_track2"].children["cam_dir2"]
        own.alignAxisToVect(own.worldPosition - target.worldPosition,0,1.0) # point X axis at target
    else:
        own.alignAxisToVect(own.parent.worldOrientation.col[0],0,1.0) # use parent Y as up axis
    own.alignAxisToVect(own.parent.worldOrientation.col[1],1,1.0) # use parent Y as up axis

def AI_target_aim(cont):
    own = cont.owner
    if not own.parent["normal"]:
        try:
            target = logic.getCurrentScene().objects.from_id(own.parent["attacker_ID"])
            own.alignAxisToVect(own.worldPosition - target.worldPosition,0,1.0) # point X axis at target
            own.alignAxisToVect(own.parent.worldOrientation.col[1],1,1.0) # use parent Y as up axis
        except:
            own.parent["normal"] = True

def shoot(cont):
    own = cont.owner
    ray = cont.sensors["shoot_ray"]
    parent = own.parent
    item = parent["item"]
    if own["AIM"]:
        if ray.positive and item != 0 and item != 3 and id(ray.hitObject) != id(parent): #alert target
            angle = ray.hitObject.worldOrientation.to_euler().z - own.worldOrientation.to_euler().z
            if math.radians(-180) <= angle < math.radians(-90) or math.radians(180) >= angle > math.radians(90): #check if target looking
                ray.hitObject["normal"] = False
                ray.hitObject["attacker_ID"] = id(parent)

    if parent["hit_released"]: #shoot
        scene = logic.getCurrentScene()
        if item == 1:
            shoot_setup(own, scene, "snow_ball", "snow", 2000)
        elif item == 2:
            shoot_setup(own, scene, "ice_cube", "ice", 3000)

def hit(cont):
    own = cont.owner
    if own.parent["item"] == 0 or own.parent["item"] == 3:
        hit = logic.getCurrentScene().addObject("hit",own,3)
        hit["owner_ID"] = id(own.parent)
        hit.setLinearVelocity([-45,0,0], True)
        own.parent["hit_released"] = False
