# Subscriptions
import math
for _ in range(int(input())):
    n, x = map(int,input().split())
    
    subscription = (n // 6) + (1 if n % 6 != 0 else 0)
    #subscription = math.ceil(n/6)
    
    total_cost = subscription * x
    
    print(total_cost)