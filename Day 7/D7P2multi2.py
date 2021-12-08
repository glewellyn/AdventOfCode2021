import time
import multiprocessing

input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

def calculate_fuel_for_position(center_position):
    min_fuel_use=-1
    for position in input:
        fuel_use=0
        distance=abs(position-center_position)
        fuel_use+=((distance**2)+distance)/2
        if fuel_use < min or min_fuel_use == -1:
            min_fuel_use = fuel_use
    print(min_fuel_use)

threadpool = 1
n = int(len(input)/threadpool)+1
center_position=range(min(input), max(input))
 
start_time = time.time()

pool = multiprocessing.Pool(threadpool)
result = pool.map(func=calculate_fuel_for_position, iterable=center_position, chunksize=n)
pool.close()
pool.join()
 
end_time = time.time()
print(end_time-start_time)