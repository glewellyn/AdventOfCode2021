def fuel_use_for_position(center_position, result, index):
    # if index % 10000 == 0 : print(index)
    fuel_use=0
    for crab_position in input:
        distance=abs(crab_position-center_position)
        fuel_use+=((distance**2)+distance)/2
    result[index] = fuel_use

from threading import Thread

global input
input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

threads = [None] * ((max(input)-min(input))+1)  # 1 thread for every position between the lowest and higest values
results = [None] * ((max(input)-min(input))+1)  # 1 result for every thread
min_input=min(input)

for i in range(len(threads)):
    threads[i] = Thread(target=fuel_use_for_position, args=((min_input+i), results, i))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()

print(results)
print(min(results))