# Water Filling
# cook your dish here
for _ in range(int(input())):
    a , b ,c = map(int,input().split())
    d = a + b + c
    if d >= 2 :
        print("Not now")
    else:
        print("Water filling time")