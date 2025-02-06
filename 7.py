# CRED Coins
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    z = x * y
    bag_worth = 100
    if z < bag_worth :
        print(0)
    else:
        r = z // 100
        print(r)
    