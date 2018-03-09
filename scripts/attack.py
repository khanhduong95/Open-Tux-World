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
from random import randint
import math

logic = common.logic
scene = logic.getCurrentScene()

def shoot_setup(own, body, scene, name, name_inventory, mass):
    body["hit_released"] = False
    shoot = scene.addObject(name+"_physics", own.parent, common.ITEM_COLLECT_EXPIRE)
    shoot.worldScale = [0.197, 0.197, 0.197]
    shoot["owner_ID"] = id(body)
    shoot.mass = mass
    shoot.setLinearVelocity([-90, 0, 0], True)
    body[name_inventory] -= 1

def target_aim(cont):
    own = cont.owner
    shoot_point = own.parent
    body = shoot_point.parent
    if own["aim"]:
        target = body.children["camera_track"].children["camera_track2"].children["cam_dir2"]
        shoot_point.alignAxisToVect(shoot_point.worldPosition - target.worldPosition, 0, 1.0) # point X axis at target
    else:
        shoot_point.alignAxisToVect(body.worldOrientation.col[0], 0, 1.0) # use body Y as up axis
    shoot_point.alignAxisToVect(body.worldOrientation.col[1], 1, 1.0) # use body Y as up axis

def AI_target_aim(cont):
    own = cont.owner
    shoot_point = own.parent
    body = shoot_point.parent
    if not body["normal"]:
        try:
            target = scene.objects.from_id(body["attacker_ID"])
            shoot_point.alignAxisToVect(shoot_point.worldPosition - target.worldPosition, 0, 1.0) # point X axis at target
            shoot_point.alignAxisToVect(body.worldOrientation.col[1], 1, 1.0) # use body Y as up axis
        except:
            return

def shoot(cont):
    own = cont.owner
    ray = cont.sensors["shoot_ray"]
    body = own.parent.parent
    body_id = id(body)
    item = body["item"]
    if own["aim"]:
        if ray.positive and item != 0 and item != 3 and id(ray.hitObject) != body_id: #alert target
            angle = ray.hitObject.worldOrientation.to_euler().z - own.worldOrientation.to_euler().z
            if math.radians(-180) <= angle < math.radians(-90) or math.radians(180) >= angle > math.radians(90): #check if target looking
                ray.hitObject["normal"] = False
                ray.hitObject["attacker_ID"] = body_id

    if ray.positive and id(ray.hitObject) != body_id and body.getDistanceTo(ray.hitObject) < 5: #too close to shoot
        return
    
    if body["hit_released"]: #shoot
        if item == 1:
            shoot_setup(own, body, scene, "snow_ball", "snow", 15)
        elif item == 2:
            shoot_setup(own, body, scene, "ice_cube", "ice", 20)

def hit(cont):
    own = cont.owner
    parent = own.parent
    hit = scene.addObject("hit", own, 3)
    hit["owner_ID"] = id(parent)
    hit.setLinearVelocity([-45, 0, 0], True)
    parent["hit_released"] = False

def check_clear(cont):
    ray = cont.sensors["shoot_ray"]
    own = cont.owner
    own["clear"] = ray.positive and id(ray.hitObject) == own.parent.parent["attacker_ID"]
