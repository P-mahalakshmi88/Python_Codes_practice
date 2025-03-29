# Chef Eren

# cook your dish here
t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    odd = (n + 1) // 2
    even = n // 2
    res = (odd * b) + ( even * a)
    print(res)