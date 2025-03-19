# The Last Levels
# cook your dish here
t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    r = x * y
    s = (x-1) // 3
    r += s * z 
    print(r)
    
        