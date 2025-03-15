# Complementary Strand in a DNA
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    n = input()
    s = ''
    for i in n :
        if i == 'A':
            s += 'T'
        elif i == 'C':
            s += 'G'
        elif i == 'T':
            s += 'A'
        else:
            s += 'C'
    print(s)
    