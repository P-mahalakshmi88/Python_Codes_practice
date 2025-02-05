# Mahasena
# cook your dish here
N = int(input())
A = list(map(int,input().split()))
lucky_count = 0
unlucky_count = 0
for i in A :
    if i % 2 == 0:
        lucky_count += 1
    else:
        unlucky_count += 1
if (lucky_count > unlucky_count):
    print('READY FOR BATTLE')
else:
    print('NOT READY')