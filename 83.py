

#Minimum number of Flips

# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int,input().split())
    s = abs(sum(a))
    r = s // 2
    if s % 2 == 0:
        print(r)
    else:
        print(-1)