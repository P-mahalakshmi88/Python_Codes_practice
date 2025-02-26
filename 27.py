# Qualify the round

t = int(input())
for _ in range(t):
    x , a , b = map(int,input().split())
    c = a * 1
    d = b * 2
    e = c + d 
    if e >= x :
        print('Qualify')
    else:
        print('NotQualify')