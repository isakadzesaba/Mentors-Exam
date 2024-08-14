def check_array(arr):
    if not arr:
        return True

    for i in arr:

        if isinstance(i, int):
            continue

        elif isinstance(i, float) and i.is_integer():
            continue
        else:
            return False

    return True

print(check_array(["-1"]))