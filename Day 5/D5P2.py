input = open('input.txt', 'r')                                                      # Read input file
lines = input.readlines()

vector_number=0
vectors=[]
for line in lines:
    vectors.append(line.replace('\n',"").replace(" -> ",",").split(","))            # Place the vectors into a list

for i in range(len(vectors)):                                                       # Convert the list of strings into a list of integers
        vectors[i] = list(map(int, vectors[i]))

max_x_position=0                                                                    # Determine required array size
max_y_position=0
for vector in vectors:
    max_x_position = max(max_x_position, vector[0], vector[3])
    max_y_position = max(max_y_position, vector[0], vector[3])
print("Array Size: " + str(max_x_position) + "x" + str(max_y_position))

diagram = [[0 for _ in range(max_x_position+1)] for _ in range(max_y_position+1)]

for vector in vectors:                                                              # Fill the diagram with the vectors
    x_start=vector[0]
    y_start=vector[1]
    x_end=vector[2]
    y_end=vector[3]
    number_of_cells=max( abs(x_start - x_end), abs(y_start-y_end)) + 1              # Determine the number of cells this vector will fill
    if x_start < x_end:                                                             # Determine X-direction
        x_direction=1
    elif x_start > x_end:
        x_direction=-1
    else:
        x_direction=0
    if y_start < y_end:                                                             # Determine Y-direction
        y_direction=1
    elif y_start > y_end:
        y_direction=-1
    else:
        y_direction=0
    for i in range(number_of_cells):
        diagram[y_start + (i * y_direction)][x_start + (i * x_direction)]+=1

overlap_count=0
for row in diagram:
    output=""
    for position in row:
        if position==0:
            output+="."
        else:
            output+=str(position)
        if position>=2:
            overlap_count+=1
    # print(output)
print("Number of overlapping points: " + str(overlap_count))