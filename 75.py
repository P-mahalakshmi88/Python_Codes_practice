
# Small Factorial

t = int(input())
for _ in range(t):
    n = int(input())
    count = 1
    for i in range(1, n + 1):
        count *= i 
        
    print(count)
        