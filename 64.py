# Speed Limit Test
# cook your dish here
import math
t = int(input())
for _ in range(t):
    a,x,b,y = map(int,input().split())
    s = a / x 
    r = b / y 
    if s > r :
        print("Alice")
    elif r > s :
        print("Bob")
    else:
        print("Equal")
        