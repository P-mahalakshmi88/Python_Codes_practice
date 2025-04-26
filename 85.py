
# Best of Two

# cook your dish here
for _ in range(int(input())):
    n = list(map(int,input().split()))
    a = n[ :-3]
    b = n[-3 : ]
    largest = -float('inf')
    second_lar = -float('inf')
    for i in a:
        if i >= largest :
            second_lar = largest 
            largest = i
        elif i > second_lar:
            second_lar = i
    sum1 = largest + second_lar
    largest1 = -float('inf')
    second_lar1 = -float('inf')
    for i in b:
        if i >= largest1 :
            second_lar1 = largest1 
            largest1 = i
        elif i > second_lar1:
            second_lar1 = i
    sum2 = largest1 + second_lar1
    
    if sum1 > sum2 :
        print('Alice')
    elif sum2 > sum1 :
        print('Bob')
    else:
        print('Tie')
   