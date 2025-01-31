# Greater Average
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    average = (a+b)/2
    if (average > c):
        print('YES')
    else:
        print('NO')