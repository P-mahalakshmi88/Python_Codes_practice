
#Chefland Games
T = int(input())
for _ in range(T):
    a,b,c,d = map(int,input().split())
    r = a + b + c + d
    if r == 0 :
        print("IN")
    else:
        print("OUT")