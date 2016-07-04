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
from scripts import collect

def main(cont):
    own = cont.owner
    own["HIT"] = own["hit_released"] = own["RUN"] = False
    if own["fish"] > 0:
        collect.generate(cont, own, 3, own["fish"], logic.getCurrentScene())
        own["fish"] = 0
    if own["ice"] > 0:
        collect.generate(cont, own, 2, own["ice"], logic.getCurrentScene())
        own["ice"] = 0
    if own["snow"] > 0:
        collect.generate(cont, own, 1, own["snow"], logic.getCurrentScene())
        own["snow"] = 0
    own.state = logic.KX_STATE5
