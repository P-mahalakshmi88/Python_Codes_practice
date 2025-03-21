# Fill Candies
# cook your dish here
import math
for _ in range(int(input())):
    n, k, m = map(int, input().split())
    s = k * m
    r = n / s
    print(math.ceil(r))
    