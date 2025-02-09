#Minimum Pizzas

for _ in range(int(input())):
    n,x = map(int,input().split())
    r = n * x
    s = r // 4
    if r % 4 != 0 :
        print(s+1)
    else:
        print(s)
        