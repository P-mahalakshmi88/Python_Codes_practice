# Chef and Water Bottles
# cook your dish here
t = int(input())
for _ in range(t):
    n , x , k = map(int,input().split())
    r = k // x
    if r <= n :
        print(r)
    else:
        print(n)
