#X Jumps
# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int,input().split())
    s = x // y
    r = x % y
    print(s + r)