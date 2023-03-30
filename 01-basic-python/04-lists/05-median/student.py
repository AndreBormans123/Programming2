# Write your code here
def median(ns):
    ns.sort()
    if len(ns) % 2:
        midden = len(ns) // 2
        return ns[midden]
    else:
        a = len(ns) // 2 - 1
        b = a + 1
        average = (ns[a] + ns[b]) / 2
        return average

    
# [1, 2, 2, 4, 4,  4 , 5  , 5, 6, 6, 7, 9]
# 12 elementen  
