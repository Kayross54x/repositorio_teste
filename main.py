import os
import sys

def process_data(d, t, y, n):
    res = []
    if t == 1:
        for i in range(len(d)):
            if d[i] > y:
                res.append(d[i] * n)
    elif t == 2:
        for i in range(len(d)):
            if d[i] < y:
                res.append(d[i] + n)
    else:
        return None
    
    print(res)
    return res

data = [10, 20, 30, 40, 50, 60]
process_data(data, 1, 25, 2)