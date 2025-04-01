# Self Defence Training
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    count = 0
    for i in range(len(x)):
        if 10 <= x[i] <= 60:
            count += 1
    print(count)