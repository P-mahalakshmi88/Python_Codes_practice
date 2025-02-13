# Sugarcane Juice Business
t = int(input())
for _ in range(t):
    n = int(input())
    total = 50 * n 
    a = (20 / 100) * total
    b = (20 / 100) * total
    c = (30 / 100) * total
    profit = total - (a + b + c)
    print(int(profit))