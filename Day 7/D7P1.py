import statistics

input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

print(input)
position_median = statistics.median(input)
print(position_median)

fuel_use=0
for position in input:
    fuel_use+=abs(position-position_median)
print(fuel_use)