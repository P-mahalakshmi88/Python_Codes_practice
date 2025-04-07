# Second Largest
t = int(input())
for _ in range(t):
    arr = map(int,input().split())
    largest = -float('inf') 
    second_largest = -float('inf')
    for i in arr :
        if i >= largest :
            second_largest = largest
            largest = i 
        elif i >= second_largest:
            second_largest = i 
    print(second_largest)
            