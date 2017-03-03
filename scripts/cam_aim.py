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
from bge import logic, events

def main(cont):
    own = cont.owner
    start_aim = own["start_aim"]
    cam_pos = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_pos"]
    if not own["fall"] and own.children["Armature"]["aim"]:
        cont.activate(cont.actuators["forward_dir"])
        cont.activate(cont.actuators["Mouse"])
        if start_aim != 8:
            cam_pos.applyMovement([-1.2,0,0], True)
            start_aim += 1

    elif start_aim != 0:
        cam_pos.applyMovement([1.2,0,0],True)
        start_aim -= 1

    own["start_aim"] = start_aim
