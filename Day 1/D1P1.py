input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

increase_count = 0
prev_number = int(lines[0].strip())
for line in lines:
    number = int(line.strip())                              # Reads number from the lina and strips the newline character
    if number > prev_number:
        increase_count += 1 
    prev_number = number

print (increase_count)