# Elections in Chefland

t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = map(int,input().split())
    count = 0
    for i in a:
        if i >= x :
            count += 1
    print(count)
            