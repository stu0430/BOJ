from math import *

d, h, w= map(int, input().split())

x = sqrt(pow(d, 2) / (pow(h, 2) + pow(w, 2)))

print(floor(h * x), floor(w * x))