from colorama import init
from termcolor import colored
init()

input = open('input.txt', 'r')                          # Read input file
input = input.readlines()

for i in range(len(input)):                             # Remove the newline characters from the input
    input[i]=input[i].replace('\n',"")     

floormap=[]                                             # Build up a list of lists of the floormap
for line in input:
    floormap_row = []
    for number in line:
        floormap_row.append(int(number))
    floormap.append(floormap_row)

low_points=[]
for y in range(len(floormap)):
    for x in range(len(floormap[y])):
        if y >= 1:   above=floormap[y-1][x]
        else:   above=10
        if x >= 1:   left=floormap[y][x-1]
        else:   left=10
        if x == len(floormap[y]) - 1:   right=10
        else:   right=floormap[y][x+1]
        if y == len(floormap) - 1:   below=10
        else:   below=floormap[y+1][x]
        if floormap[y][x] < min(above, left, right, below):
            low_points.append(floormap[y][x])

solution=0
for low_point in low_points:
    solution += low_point + 1
print(solution)
    