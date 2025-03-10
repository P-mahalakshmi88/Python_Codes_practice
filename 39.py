# Finding shoes

t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    if m < n :
       left = n - m
    else :
        left = 0
    right = n
    print(left + right)
    