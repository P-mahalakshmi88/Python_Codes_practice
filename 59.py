# Minimum number of coins

# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    if x % 5 != 0:
        print(-1)
    else:
        s = x // 10
        p = x % 10
        if p == 0:
            print(s)
        else:
            r = p // 5
            print(s + r)