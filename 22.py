# Air Conditioner Temperature
t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if b >= a  and b >= c :
        print('Yes')
    else:
        print('No')