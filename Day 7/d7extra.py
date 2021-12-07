import statistics
import random

for y in range(1000000):
    input=[]
    input_length=random.randint(10, 200)
    for i in range(input_length):
        input.append(random.randint(1,2000))

    #elegant solution
    position_mean = int(statistics.mean(input))
    min_fuel_use=[]
    for i in range(position_mean, position_mean+2):
        fuel_use=0
        for position in input:
            distance=abs(position-i)
            fuel_use+=((distance**2)+distance)/2
        min_fuel_use.append(fuel_use)
    elegant = int(min(min_fuel_use))

    #brute force solution
    min_fuel_use=[]
    for i in range(min(input), max(input)+1):
        fuel_use=0
        for position in input:
            distance=abs(position-i)
            fuel_use+=((distance**2)+distance)/2
        min_fuel_use.append(fuel_use)
    brute=int(min(min_fuel_use))
    
    if y % 1000 == 0:
        print(y)

    if elegant != brute:
        print(input)
        break
