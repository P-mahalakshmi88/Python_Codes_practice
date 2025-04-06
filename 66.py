#A or B
t = int(input())
for _ in range(t):
    x , y = map(int,input().split())
    a = x 
    b = x + y 
    c = y  
    d = y + x
    p = 500 - (a * 2) + 1000 - (b * 4)
    q = 500 - (c * 4) + 1000 - (d * 2)
    print(max(p , q))