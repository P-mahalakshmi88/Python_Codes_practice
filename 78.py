
# Chef And Operators

T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    if a < b:
        print("<")
    elif (a > b):
        print(">")
    else:
        print("=")
