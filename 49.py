# Blackjack
# cook your dish here
for _ in range(int(input())):
    a , b = map(int,input().split())
    c = 21 -(a+b)
    if c <= 10:
        print(c)
    else:
        print(-1)