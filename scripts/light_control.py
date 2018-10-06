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
def main(cont):
    own = cont.owner
    sun = own.children["sun"]
    moon = own.children["moon"]
    sun_sky = sun.children["sun_sky"]
    moon_sky = moon.children["moon_sky"]
    delay = cont.sensors["Delay"]
    hour = own["hour"]
    minute = own["minute"]
    if delay.positive:
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
    #daytime = 6 <= hour < 18
    if 6 <= hour < 18:
        if sun.energy < 1:
            sun.energy += 0.01
            sun_sky.energy += 0.01
        if moon.energy > 0:
            moon.energy -= 0.002
            moon_sky.energy -= 0.002
    else:
        if sun.energy > 0:
            sun.energy -= 0.01
            sun_sky.energy -= 0.01
        if moon.energy < 0.3:
            moon.energy += 0.002
            moon_sky.energy += 0.002
    # elif 7 <= hour < 8 or 16 <= hour < 17:
    #     moon.energy = 0.0
    #     sun.energy = 0.75
    #     moon_sky.energy = 0.0
    #     sun_sky.energy = 0.75
    # elif 6 <= hour < 7 or 17 <= hour < 18:
    #     moon.energy = 0.0
    #     sun.energy = 0.5
    #     moon_sky.energy = 0.0
    #     sun_sky.energy = 0.5
    # elif 5 <= hour < 6 or 18 <= hour < 19:
    #     moon.energy = 0.1
    #     sun.energy = 0.25
    #     moon_sky.energy = 0.1
    #     sun_sky.energy = 0.5
    # else:
    #     moon.energy = 0.3
    #     sun.energy = 0.0
    #     moon_sky.energy = 0.3
    #     sun_sky.energy = 0.0

    own["hour"] = hour
    own["minute"] = minute
    #own["daytime"] = daytime
