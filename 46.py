# Candy Distribution
# cook your dish here
import math
t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    r = n // m 
    if n % m == 0:
        if r % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print('NO')