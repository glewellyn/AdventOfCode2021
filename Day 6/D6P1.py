input = open('input.txt', 'r')                  # Read input file
input = input.readlines()
input = input[0].split(",")                     # Convert the list of strings into a list of integers
input = list(map(int, input))

ages = [0 for _ in range(9)]                    # Create list containing the age groups
for i in range(0,7):                            # Count the number of fish every age
    ages[i]=input.count(i);                     # Place that number in the corresponding place in the list

for i in range(256):
    reproducing_fish=ages[0]                    # Store the number of reproducing fish
    del ages[0]                                 # Remove the first item in the list, moving all ages to one age lower
    ages.append(reproducing_fish)               # Place the offspring into age group 8
    ages[6]+=reproducing_fish                   # Add the fish that have reproduced into group 6

print(sum(ages))