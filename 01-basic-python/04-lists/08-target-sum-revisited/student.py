# Write your code here
def target_sum(ns, target):
    seen = set()
    for num in ns:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False
