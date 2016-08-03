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
    if col.positive and id(col.hitObject) != own["owner_ID"]:
        hitobj = col.hitObject
        print(hitobj)
        if "penguin" in hitobj:
            hitobj["health"] -= own.mass*0.001
            if "AI" in hitobj:
                hitobj["normal"] = False
                hitobj["attacker_ID"] = own["owner_ID"]
        own.endObject()

def hit(cont):
    own = cont.owner
    col = cont.sensors["Collision"]
    if col.positive and id(col.hitObject) != own["owner_ID"]:
        hitobj = col.hitObject
        if "penguin" in hitobj:
            hitobj["health"] -= own.mass*0.0001
            if "AI" in hitobj:
                hitobj["normal"] = False
                hitobj["attacker_ID"] = own["owner_ID"]
