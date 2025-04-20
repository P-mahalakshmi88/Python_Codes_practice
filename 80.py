
# Reach fast

import math
T= int(input())
for _ in range(T):
    a,b,k = map(int,input().split())
    if a != b :
        print(math.ceil(abs(a - b) / k))
    else :
        print(0)