# Exams
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    a = x*y
    r = ((z/a)*100)
    if r > 50 :
        print('YES')
    else:
        print('NO')