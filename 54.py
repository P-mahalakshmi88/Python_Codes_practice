# It is My Serve
t = int(input())
for _ in range(t):
    p , q = list(map(int,input().split()))
    s = p + q
    r = s // 2
    if r % 2 == 0:
        print("Alice")
    else:
        print("Bob")
    