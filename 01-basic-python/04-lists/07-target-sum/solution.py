def target_sum(ns, target):
    for x in ns:
        for y in ns: #eindigt eerst loop y dan loop x dan weer loop y enz
            if x + y == target:
                return True
    return False

