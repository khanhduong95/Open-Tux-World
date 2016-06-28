from bge import logic

def aim_move(own, FORWARD, BACK, LEFT, RIGHT, started_aim, current_frame):
    if FORWARD:
        if LEFT:
            if current_frame <= 70:
                current_frame = 70

            elif current_frame >= 120:
                current_frame = 80
            own.playAction("lower_aim", current_frame, current_frame+1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 1

        elif RIGHT:
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

    elif BACK:
        if LEFT:
            if current_frame >= 190:
                current_frame = 190

            elif current_frame <= 140:
                current_frame = 180
            own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame -= 1

        elif RIGHT:
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

    elif LEFT:
        if current_frame >= 250:
            current_frame = 250

        elif current_frame <= 200:
            current_frame = 240
        own.playAction("lower_aim", current_frame, current_frame-1, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        current_frame -= 1

    elif RIGHT:
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

def move(own, FORWARD, BACK, LEFT, RIGHT, started_aim, current_frame):

    if FORWARD or BACK or LEFT or RIGHT:
        if own["RUN_FAST"]:
            if current_frame <= 0:
                current_frame = 0
            elif current_frame >= 42:
                current_frame = 14
            own.playAction("run", current_frame, current_frame+2, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
            current_frame += 2

        elif own["RUN"]:
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

def action(cont):
    own = cont.owner
    upper_frame = own["upper_frame"]
    hit = own["HIT"]
    hit_released = own.parent["hit_released"]
    if own.parent["death"]:
        own.state = logic.KX_STATE2

    elif own["FALL"]:
        if upper_frame <= 0:
            own.playAction("upper_aim", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_frame = 0
        else:
            own.playAction("upper_aim", upper_frame, upper_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
            upper_frame -= 1

    else:
        if own["AIM"]:
            if own.parent["HIT"] or (hit and upper_frame < 30):
                if upper_frame < 10:
                    upper_frame = 10
                own.playAction("upper_aim", upper_frame, upper_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_frame += 1
                hit = True
            elif hit and upper_frame == 30:
                upper_frame = 10
                hit_released = True
                hit = False
            else:
                if upper_frame >= 10:
                    own.playAction("upper_aim", 10, 10, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_frame = 10
                else:
                    own.playAction("upper_aim", upper_frame, upper_frame+1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_frame += 1

        else:
            if own.parent["HIT"] or (hit and upper_frame < 30):
                if upper_frame < 10:
                    upper_frame = 10
                own.playAction("upper_aim", upper_frame, upper_frame+1, layer=2, play_mode=logic.KX_ACTION_MODE_PLAY)
                upper_frame += 1
                hit = True
            elif hit and upper_frame == 30:
                upper_frame = 10
                hit_released = True
                hit = False
            else:
                if upper_frame <= 0:
                    own.playAction("upper_aim", 0, 0, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_frame = 0
                else:
                    own.playAction("upper_aim", upper_frame, upper_frame-1, layer=1, play_mode=logic.KX_ACTION_MODE_PLAY)
                    upper_frame -= 1

    own["HIT"] = hit
    own.parent["hit_released"] = hit_released
    own["upper_frame"] = upper_frame

def main(cont):
    own = cont.owner
    if own["FALL"]:
        own.playAction("fall", 7, 7, layer=0, play_mode=logic.KX_ACTION_MODE_PLAY)
        own["started_aim"] = 0

    else:
        FORWARD = own["FORWARD"]
        BACK = own["BACK"]
        LEFT = own["LEFT"]
        RIGHT = own["RIGHT"]
        started_aim = own["started_aim"]
        current_frame = own["current_frame"]

        if own["AIM"]:
            aim_move(own, FORWARD, BACK, LEFT, RIGHT, started_aim, current_frame)
        else:
            move(own, FORWARD, BACK, LEFT, RIGHT, started_aim, current_frame)