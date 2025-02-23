# reverse the number
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = (rev * 10) + remainder
        n = n // 10
    print(rev)