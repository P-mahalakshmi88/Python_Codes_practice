# Flip the cards
# cook your dish here
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    y = n - x
    if y >= x :
        print(x)
    elif y < x:
        print(y)
    else:
        print(0)