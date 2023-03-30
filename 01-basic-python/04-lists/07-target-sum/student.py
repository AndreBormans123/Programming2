# Write your code here
def target_sum(ns, target):
    for i in ns:
        for x in ns:
            if x + i == target:
                return True
            
    return False

