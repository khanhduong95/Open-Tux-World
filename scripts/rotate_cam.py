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
import math

def aim(rot_aim, cam_dir, collision, aim):
    if aim:
        if collision:
            if rot_aim < 10:
                cam_dir.applyRotation([0,0,math.radians(-0.25)],True)
                rot_aim += 1
        else:
            if rot_aim > 0:
                cam_dir.applyRotation([0,0,math.radians(0.25)],True)
                rot_aim -= 1
    else:
        if rot_aim < 5:
            cam_dir.applyRotation([0,0,math.radians(-0.25)],True)
            rot_aim += 1
        elif rot_aim > 5:
            cam_dir.applyRotation([0,0,math.radians(0.25)],True)
            rot_aim -= 1

    cam_dir["rot_aim"] = rot_aim

def main(cont):
    own = cont.owner
    cam_dir = own.children["cam_dir2"]
    rot = cam_dir["rot"]
    rot_aim = cam_dir["rot_aim"]
    col = own["collision"]
    if col:
        if rot < 10:
            cam_dir.applyRotation([0,0,math.radians(-0.4)],True)
            rot += 1
    else:
        if rot > 0:
            cam_dir.applyRotation([0,0,math.radians(0.4)],True)
            rot -= 1

    aim(rot_aim, cam_dir, col, own.parent.parent.children["Armature"]["AIM"])
    cam_dir["rot"] = rot
