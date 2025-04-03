# Too many Floors
# cook your dish here
import math
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    s = x / 10
    r = y / 10
    p = math.ceil(s) - math.ceil(r)
    print(abs(p))  # abs - it converts negative to positive
    
    
# t = int(input())
# for _ in range(t):
#     x, y = map(int, input().split())
#     floor_x = (x - 1) // 10 + 1
#     floor_y = (y - 1) // 10 + 1
#     print(abs(floor_x - floor_y))