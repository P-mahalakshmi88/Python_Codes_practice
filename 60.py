#Airlines
# cook your dish here
import math
t = int(input())
for _ in range(t):
    x,n = map(int,input().split())
    s = n / 100
    r = math.ceil(s) - x
    if r > 0:
        print(r)
    else:
        print(0)