
# Get Lowest Free
# cook your dish here
t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    s = min(arr)
    print(sum(arr) - s)
    
    # arr.sort()
    # print(arr[1] + arr[2])