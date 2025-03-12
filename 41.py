# Mario and Transformation
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 3 == 0 :
        print("NORMAL")
    elif n % 3 == 1 :
        print("HUGE")
    else:
        print("SMALL")
    