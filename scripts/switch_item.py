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
    item = own["item"]
    if previous:
        item = check_item_previous(own, item-1)
    elif next:
        item = check_item_next(own, item+1)
    else:
        item = check_item_previous(own, item)
    own["item"] = item
