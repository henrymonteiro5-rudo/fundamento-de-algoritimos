from math import sqrt
import math

def resultado (a, b, c):
    r = math.sqrt(a) + math.sqrt(b) + math.sqrt(c) + (a + b)/2 + (b + c)/2 + (a + c)/2
    return r

x = resultado(4, 16, 36)
print(x)