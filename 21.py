# Problems in your to-do list
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    x = map(int, input().split())
    count = 0
    for i in x :
        if i >= 1000:
            count+=1 
    print(count)