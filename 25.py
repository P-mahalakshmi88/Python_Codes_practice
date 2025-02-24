# Sasta Shark Tank
# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    a = x * 10
    b = y * 5
    if a > b :
        print("FIRST")
    elif b > a:
        print("SECOND")
    else:
        print("ANY")