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

def shoot(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    if col.positive and id(col.hitObject) != own["owner_ID"]:
        reduce_health(own, col.hitObject)
        own.endObject()
        
    else:
        v = own.worldLinearVelocity
        hitPos = own.rayCast(own.worldPosition + v, own, common.getDistance(v) / 30, "", 0, 0, 0)
        hitObj = hitPos[0]
        if hitObj and id(hitObj) != own["owner_ID"]:
            hitObj.applyImpulse(hitPos[1], v * own.mass, False)
            reduce_health(own, hitObj)
            own.endObject()            

def hit(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    if col.positive and id(col.hitObject) != own["owner_ID"]:
        reduce_health(own, col.hitObject)

def reduce_health(own, hitObj):
    if "penguin" in hitObj:
        hitObj["health"] -= own.mass*0.01
        if "AI" in hitObj:
            hitObj["normal"] = False
            hitObj["attacker_ID"] = own["owner_ID"]
