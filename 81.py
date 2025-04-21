
# Single-use Attack
# cook your dish here
t = int(input())
for _ in range(t):
    h,x,y = map(int,input().split())
    remaining_health = h - y
    
    if remaining_health <= 0:
        print(1)
    else:
        normal_attacks = (remaining_health + x - 1) // x
        print(1 + normal_attacks)