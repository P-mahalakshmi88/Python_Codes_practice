#Minimum Cars required
# cook your dish here
import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = n / 4
    b = math.ceil(a)
    print(b)