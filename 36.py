# Police and Thief

# cook your dish here
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a > b:
        print(a - b)
    elif b > a:
        print(b - a)
    else:
        print(0)