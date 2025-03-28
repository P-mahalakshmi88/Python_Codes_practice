# Chef and his Apps

# cook your dish here
t = int(input())
for _ in range(t):
    s,x,y,z = map(int,input().split())
    r = x+y 
    unuse_mem = s - r 
    if unuse_mem >= z:
        print(0)
    elif unuse_mem +x >= z or unuse_mem + y >=z:
        print(1)
    else:
        print(2)
    
    