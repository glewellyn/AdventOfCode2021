input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

number_of_lines = len(lines)

def sum_of_lines(startline):
    total = int(lines[startline])
    total += int(lines[startline+1])
    total += int(lines[startline+2])
    return total

increase_count = 0
prev_total = sum_of_lines(0)

for i in range (0, (len(lines))-2):
    total = sum_of_lines(i)
    if total > prev_total:
        increase_count += 1 
    prev_total = total

print (increase_count)