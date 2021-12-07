input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

diag_report = []
diag_report2 = []
line_number = 0

for line in lines:                                          # Fill the list of lists
    diag_report.append(list(line))
    diag_report2.append(list(line))

for line in diag_report:
    line.pop()

for line in diag_report2:
    line.pop()

line_length = len(diag_report[0])

for i in range(line_length):                                # Oxygen Generator calculation
    column_total=0
    for line in diag_report:                                # Determine most occurring digit
        column_total+=int(line[i])
    if column_total >= len(diag_report)/2:
        most_ocurring=1
    else:
        most_ocurring=0
    for j in reversed(range(len(diag_report))):              # Remove lines with least ocurring digit
        if int(diag_report[j][i]) != most_ocurring:
            del diag_report[j]
    if len(diag_report) <= 1: break

for i in range(line_length):                                 # CO2 Scrubber calculation
    column_total=0
    for line in diag_report2:                                # Determine most occurring digit
        column_total+=int(line[i])
    if column_total < len(diag_report2)/2:
        least_ocurring=1
    else:
        least_ocurring=0
    for j in reversed(range(len(diag_report2))):              # Remove lines with least ocurring digit
        if int(diag_report2[j][i]) != least_ocurring:
            del diag_report2[j]
    if len(diag_report2) <= 1: break

oxygen_generator = ""
for i in range(len(diag_report[0])):
    oxygen_generator += diag_report[0][i]
   
co2_scrubber = ""   
for i in range(len(diag_report2[0])):
    co2_scrubber += diag_report2[0][i]

print("Oxygen Generator: " + oxygen_generator + "  Decimal: " + str(int(oxygen_generator,2)))
print("CO2 Scrubber: " + co2_scrubber + "  Decimal: " + str(int(co2_scrubber,2)))
print("Oxygen Generator * CO2 Scrubber = " + str(int(oxygen_generator,2) * int(co2_scrubber,2)))
