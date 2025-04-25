
# Binary Battles

t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    count = 0
    temp = n
    while temp > 1:
        temp //= 2
        count += 1
    total_time = (a * count) + (b * (count - 1))
    print(total_time)