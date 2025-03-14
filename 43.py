# Chess Ratings
# cook your dish here
import math
t = int(input())
for _ in range(t):
    x , y = map(int,input().split())
    z = x + 8
    if x >= y :
        print(0)
    else:
        r = math.ceil((y-x) / 8)
        print(r)
    