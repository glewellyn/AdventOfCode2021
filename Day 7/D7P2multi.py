def fuel_use_for_position(start_position, result, index, step_size):
    min_fuel_use=-1
    fuel_use=0
    counter=0
    for i in range(start_position, max(input), step_size):
        if counter % (10000*step_size) == 0 : print("Thread: " + str(index) + "    increment: " + str(counter) + "     calculating position: " + str(i) + "     lowest found: " + str(min_fuel_use))
        counter +=1
        for crab_position in input:
            distance=abs(crab_position-i)
            fuel_use+=((distance**2)+distance)/2
        if min_fuel_use == -1 or fuel_use <  min_fuel_use:
            min_fuel_use = fuel_use
    result[index] = min_fuel_use

from threading import Thread
threadcount=64

global input
input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

threads = [None] * threadcount                  # 1 thread for every position between the lowest and higest values
results = [None] * threadcount                  # 1 result for every thread
min_input=min(input)

for i in range(len(threads)):
    print("Starting Thread" + str(i))
    threads[i] = Thread(target=fuel_use_for_position, args=((min_input+i), results, i, threadcount))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()

print(results)
print(min(results))