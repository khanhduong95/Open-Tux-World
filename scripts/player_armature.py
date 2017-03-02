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

def aim_move(own, forward, back, left, right, started_aim, current_frame):
    if forward:
        if left:
            if current_frame <= 70:
                current_frame = 70

            elif current_frame >= 120:
                current_frame = 80
            own.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

        elif right:
            if current_frame <= 130:
                current_frame = 130

            elif current_frame >= 180:
                current_frame = 140
            own.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

        else:
            if current_frame <= 10:
                current_frame = 10

            elif current_frame >= 60:
                current_frame = 20
            own.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

    elif back:
        if left:
            if current_frame >= 190:
                current_frame = 190

            elif current_frame <= 140:
                current_frame = 180
            own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame -= 1

        elif right:
            if current_frame >= 130:
                current_frame = 130

            elif current_frame <= 80:
                current_frame = 120
            own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame -= 1

        else:
            if current_frame >= 70:
                current_frame = 70

            elif current_frame <= 20:
                current_frame = 60
            own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame -= 1

    elif left:
        if current_frame >= 250:
            current_frame = 250

        elif current_frame <= 200:
            current_frame = 240
        own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        current_frame -= 1

    elif right:
        if current_frame <= 190:
            current_frame = 190

        elif current_frame >= 240:
            current_frame = 200
        own.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        current_frame += 1

    else:
        if started_aim == 0:
            own.playAction("lower_aim", 0, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            started_aim = 1

        else:
            own.playAction("lower_aim", 10, 10, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)

    own["started_aim"] = started_aim
    own["current_frame"] = current_frame

def move(own, forward, back, left, right, started_aim, current_frame):

    if forward or back or left or right:
        if own["run_fast"]:
            if current_frame <= 0:
                current_frame = 0
            elif current_frame >= 42:
                current_frame = 14
            own.playAction("run", current_frame, current_frame+2, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 2

        elif own["run"]:
            if current_frame <= 0:
                current_frame = 0
            elif current_frame >= 42:
                current_frame = 14
            own.playAction("run", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

        else:
            if current_frame <= 0:
                current_frame = 0
            elif current_frame >= 77:
                current_frame = 7
            own.playAction("walk", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

    else:
        own.playAction("walk", 0, 0, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        current_frame = 0

    own["started_aim"] = started_aim
    own["current_frame"] = current_frame

def action_armed(own, fall, upper_current_frame, hit, hit_released):

    if fall:
        hit_released = False
        if upper_current_frame <= 0:
            own.playAction("upper_aim_armed", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_current_frame = 0
        else:
            own.playAction("upper_aim_armed", upper_current_frame, upper_current_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_current_frame -= 1

    else:
        if own["aim"]:
            if own.parent["hit"] or (hit and upper_current_frame < 30):
                if upper_current_frame < 10:
                    upper_current_frame = 10
                else:
                    hit_released = upper_current_frame == 24
                own.playAction("upper_aim_armed", upper_current_frame, upper_current_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_current_frame += 1
                hit = True
            elif hit and upper_current_frame == 30:
                upper_current_frame = 10
                hit = False
            else:
                if upper_current_frame >= 10:
                    own.playAction("upper_aim_armed", 10, 10, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame = 10
                else:
                    own.playAction("upper_aim_armed", upper_current_frame, upper_current_frame+1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame += 1

        else:
            if own.parent["hit"] or (hit and upper_current_frame < 30):
                if upper_current_frame < 10:
                    upper_current_frame = 10
                else:
                    hit_released = upper_current_frame == 24
                own.playAction("upper_aim_armed", upper_current_frame, upper_current_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_current_frame += 1
                hit = True
            elif hit and upper_current_frame == 30:
                upper_current_frame = 10
                hit = False
            else:
                if upper_current_frame <= 0:
                    own.playAction("upper_aim_armed", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame = 0
                else:
                    own.playAction("upper_aim_armed", upper_current_frame, upper_current_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame -= 1

    own["hit"] = hit
    own.parent["hit_released"] = hit_released
    own["upper_current_frame"] = upper_current_frame

def action_unarmed(own, fall, upper_current_frame, hit, hit_released):

    if fall:
        hit_released = False
        if upper_current_frame <= 0:
            own.playAction("upper_aim", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_current_frame = 0
        else:
            own.playAction("upper_aim", upper_current_frame, upper_current_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_current_frame -= 1

    else:
        if own["aim"]:
            if own.parent["hit"] or (hit and upper_current_frame < 30):
                if upper_current_frame < 10:
                    upper_current_frame = 10
                else:
                    hit_released = upper_current_frame == 24
                own.playAction("upper_aim", upper_current_frame, upper_current_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_current_frame += 1
                hit = True
            elif hit and upper_current_frame == 30:
                upper_current_frame = 10
                hit = False
            else:
                if upper_current_frame >= 10:
                    own.playAction("upper_aim", 10, 10, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame = 10
                else:
                    own.playAction("upper_aim", upper_current_frame, upper_current_frame+1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame += 1

        else:
            if own.parent["hit"] or (hit and upper_current_frame < 30):
                if upper_current_frame < 10:
                    upper_current_frame = 10
                else:
                    hit_released = upper_current_frame == 24
                own.playAction("upper_aim", upper_current_frame, upper_current_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_current_frame += 1
                hit = True
            elif hit and upper_current_frame == 30:
                upper_current_frame = 10
                hit = False
            else:
                if upper_current_frame <= 0:
                    own.playAction("upper_aim", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame = 0
                else:
                    own.playAction("upper_aim", upper_current_frame, upper_current_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_current_frame -= 1

    own["hit"] = hit
    own.parent["hit_released"] = hit_released
    own["upper_current_frame"] = upper_current_frame

def action(cont):
    own = cont.owner
    upper_current_frame = own["upper_current_frame"]
    hit = own["hit"]
    hit_released = own.parent["hit_released"]
    if own.parent["death"]:
        own.state = logic.KX_STATE2
    elif own.parent["item"] == 0:
        action_unarmed(own, own["fall"], own["upper_current_frame"], own["hit"], own.parent["hit_released"])
    else:
        action_armed(own, own["fall"], own["upper_current_frame"], own["hit"], own.parent["hit_released"])

def main(cont):
    own = cont.owner
    if own["fall"]:
        own.playAction("fall", 7, 7, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        own["started_aim"] = 0

    else:
        forward = own["forward"]
        back = own["back"]
        left = own["left"]
        right = own["right"]
        started_aim = own["started_aim"]
        current_frame = own["current_frame"]

        if own["aim"]:
            aim_move(own, forward, back, left, right, started_aim, current_frame)
        else:
            move(own, forward, back, left, right, started_aim, current_frame)
