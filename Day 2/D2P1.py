input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

depth = 0
forward = 0

for line in lines:
    instruction = line.split()
    if instruction[0] == "up" :
        depth -= int(instruction[1])
    elif instruction[0] == "down" :
        depth += int(instruction[1])
    else :
        forward += int(instruction[1])
        
print ("Depth: " + str(depth) + "  Forward: " + str(forward))
print ("Answer: " + str(depth*forward))