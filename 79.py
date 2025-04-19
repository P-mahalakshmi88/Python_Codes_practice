
# Mutated Minions
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    N = map(int,input().split())
    count = 0
    for i in N :
        s = k + i
        if s % 7 == 0:
            count += 1
    print(count)
