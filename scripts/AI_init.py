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

def main(cont):
    own = cont.owner
    brain = own["brain"] = randint(0,2)
    logic.globalDict["AI_list"].append(id(own))
    
    if brain != 0:
        snow_ice = randint(0,3)
        if snow_ice == 1:
            own["snow"] = 30
        elif snow_ice == 2:
            own["ice"] = 30
        elif snow_ice == 3:
            own["snow"] = 15
            own["ice"] = 15

    own["fish"] = randint(0,10)

    own["health"] = randint(60, 80)
    own.state = logic.KX_STATE2
