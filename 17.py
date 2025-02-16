# car or Bike

for i in range(int(input())):
    x , y = map(int,input().split())
    if (x > y):
        print("CAR")
    elif (y > x):
        print("BIKE")
    else:
        print("SAME")