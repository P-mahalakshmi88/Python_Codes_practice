# Monopoly
for _ in range(int(input())):
    p,q,r,s = map(int,input().split())
    a = q + r + s
    b = p + r + s 
    c = p + q + s 
    d = p + q + r
    if (a < p) or (b < q) or (c < r) or (d < s):
        print("YES")
    else:
        print("NO")
        
# if p > (q + r + s) or q > (p + r + s) or r > (p + q + s) or s > (p + q + r):
#     print("YES")
# else:
#     print("NO")
