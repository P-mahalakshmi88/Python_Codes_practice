# Water Mixing
t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    s = b - a 
    r = a - b
    if a < b :
        if  s <= x:
            print("YES")
        else:
            print("NO")
      
    else:
        if r <= y:
            print("YES")
        else:
            print("NO")
            
