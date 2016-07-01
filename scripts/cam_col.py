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
def check_ray(own, ray):
    cam = own.children["cam_holder"]
    target = own.children["cam_pos"]
    if ray.positive:
        cam.worldPosition = ray.hitPosition
    else:
        cam.worldPosition = target.worldPosition

def main(cont):
    own = cont.owner
    if own.state == 1:
        check_ray(own, cont.sensors["cam_ray"])
    else:
        check_ray(own, cont.sensors["cam_ray.001"])
