
# Endless Appetizers

import math
t = int(input())
for _ in range(t):
    x,y,r = map(int,input().split())
    z = x + (r / 30)
    print(math.ceil(z / y))