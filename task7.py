def is_valid_pin_codes(ls: list) -> bool:
    set1 = set(ls)
    if len(set1) < len(ls) or len(ls) == 0:
        return False
    for i in ls:
        if len(i) != 4 or not i.isnumeric():
            return False
    return True
