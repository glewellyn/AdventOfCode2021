import statistics

input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

#elegant solution - faulty
position_mean = int(statistics.mean(input))
min_fuel_use=[]
for i in range(position_mean, position_mean+2):
    fuel_use=0
    for position in input:
        distance=abs(position-i)
        fuel_use+=((distance**2)+distance)/2
    min_fuel_use.append(fuel_use)
print(int(min(min_fuel_use)))

#brute force solution
min_fuel_use=[]
for i in range(min(input), max(input)+1):
    fuel_use=0
    for position in input:
        distance=abs(position-i)
        fuel_use+=((distance**2)+distance)/2
    min_fuel_use.append(fuel_use)
print(int(min(min_fuel_use)))