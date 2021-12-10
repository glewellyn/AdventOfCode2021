import sys
from colorama import init
from termcolor import colored
sys.setrecursionlimit(10000)
init()

input = open('up1.txt', 'r')                          # Read input file
input = input.readlines()

for i in range(len(input)):                             # Remove the newline characters from the input
    input[i]=input[i].replace('\n',"")     

floormap=[]                                             # Build up a list of lists of the floormap
for line in input:
    floormap_row = []
    for number in line:
        if int(number) == 9:
            floormap_row.append("X")
        else:
            floormap_row.append(" ")
    floormap.append(floormap_row)

def fill_area(y,x,basin_number):
    floormap[y][x]=basin_number
                                                        # Check above the given position
    if y >= 1:                                          # Don't check row 0
        if floormap[y-1][x] == " ":                     # If it's empty
            fill_area(y-1,x,basin_number)               # Fill with basin counter

                                                        # Check left of the given position
    if x >= 1:                                          # Don't check column 0
        if floormap[y][x-1] == " ":                     # If it's empty
            fill_area(y,x-1,basin_number)               # Fill with basin counter
            
                                                        # Check right of the given position
    if x != len(floormap[y]) - 1:                       # Don't check the last column
        if floormap[y][x+1] == " ":                     # If it's empty
            fill_area(y,x+1,basin_number)               # Fill with basin counter
            
                                                        # Check below the given position
    if y != len(floormap) - 1:                                          # Don't check the bottom row
        if floormap[y+1][x] == " ":                     # If it's empty
            fill_area(y+1,x,basin_number)               # Fill with basin counter

basin_number=0
for y in range(len(floormap)):                          # Find empty position
    for x in range(len(floormap[y])):
        if floormap[y][x] == " ":
            fill_area(y, x, basin_number)               # Fill the area containing the empty position
            basin_number+=1
    
basin_sizes=[]                                          
for i in range(basin_number):                           # loop through the found basins 
    basin_size=0
    for row in floormap:                                # Loop through the floormap
        for position in row:
            if position != "X":
                if int(position)==i:
                    basin_size+=1                       # Count all positions of this basin
    basin_sizes.append(basin_size)
basin_sizes.sort(reverse=True)
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
