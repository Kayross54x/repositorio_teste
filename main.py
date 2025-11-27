import os
import sys
from utils import *

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

def process_data_two(d, t, y, n):
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
configure_system_settings("localhost", 8080, "root", "1234", "prod", 10, 3, True, "INFO", "admin@admin.com", "/tmp")