input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

diag_report = []
line_number = 0
diag_report = []

for i in range (len(list(lines[1]))-1): diag_report.append([]) # Create a list of lists

for line in lines:                                             # Fill the list of lists
    position = 0
    for number in list(line):
        if number in ["0", "1"]:
            diag_report[position].append(int(number))
        position += 1

gamma_rate = ""
epsilon_rate = ""
line_length = len(diag_report[0])

for line in diag_report:
    if line.count(1) > line_length/2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print("Gamma rate:   " + gamma_rate + "  Decimal: " + str(int(gamma_rate,2)))
print("Epsilon rate: " + epsilon_rate + "  Decimal: " + str(int(epsilon_rate,2)))

print("Gamma rate * Epsilon rate = " + str(int(gamma_rate,2) * int(epsilon_rate,2))) 