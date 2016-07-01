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

def main(cont):
    own = cont.owner
    own['stamina'] = own['max_stamina']
    own["item"] = 2
    own["snow"] = 20
    own["ice"] = 20
    scene = logic.getCurrentScene()
    scene.active_camera = own.children["camera_track"].children["camera_track2"].children["cam_dir2"].children["cam_dir"].children["cam_holder"].children["Camera"]
    own.state = logic.KX_STATE2
