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
def shoot(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    col_1 = cont.sensors["Collision.001"]
    if col.positive and id(col.hitObject) != own["owner_ID"]:
        col.hitObject["normal"] = False
        col.hitObject["attacker_ID"] = own["owner_ID"]
    if col_1.positive:
        own.setLinearVelocity([-0.00000012,0,0], True)
        own.mass *= 80000
        own.applyForce([-2000000,0,0], True)
        own.endObject()

def hit(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    if col.positive:
        if id(col.hitObject) != own["owner_ID"]:
            col.hitObject["normal"] = False
            col.hitObject["attacker_ID"] = own["owner_ID"]
