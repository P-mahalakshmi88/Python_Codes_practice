
# Chef and Races

t = int(input())
for _ in range(t):
    x,y,a,b = map(int,input().split())
     
    wins = 0
    if x != a and x != b:
        wins += 1
    if y != a and y != b:
        wins += 1
    print(wins)