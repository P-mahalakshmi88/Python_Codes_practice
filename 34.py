# Maximise the Tastiness
# cook your dish here
t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    x = max(a,b)
    y = max(c,d)
    print(x+y)
        