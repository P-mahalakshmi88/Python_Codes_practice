# Chef and Candies
for _ in range(int(input())):
    n,x = map(int,input().split())
    pac = 4
    if n <= x:
        print('0')
    elif n > x:
        s = n - x
        r = s // pac
        if s % pac != 0 :
            r += 1
        print(r)