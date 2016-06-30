def check_item_previous(own, item_number):
    if item_number == 0:
        return 0
    elif item_number == 2 or item_number < 0:
        if own["ice"] > 0:
            return 2
        else:
            return check_item_previous(own, 1)
    else:
        if own["snow"] > 0:
            return 1
        else:
            return 0

def check_item_next(own, item_number):
    if item_number == 0 or item_number > 2:
        return 0
    elif item_number == 1:
        if own["snow"] > 0:
            return 1
        else:
            return check_item_next(own, 2)
    else:
        if own["ice"] > 0:
            return 2
        else:
            return 0

def main(own, previous, next):
    if previous:
        own["weapon"] = check_item_previous(own, own["weapon"]-1)
        print(own["weapon"])
    elif next:
        own["weapon"] = check_item_next(own, own["weapon"]+1)
        print(own["weapon"])
    else:
        own["weapon"] = check_item_previous(own, own["weapon"])
