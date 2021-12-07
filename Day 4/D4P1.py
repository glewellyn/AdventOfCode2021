import numpy as numpy

input = open('input.txt', 'r')                              # Read input file
lines = input.readlines()

draw_numbers = lines[0].replace('\n',"").split(",")         # Place the draw numbers into a list
lines.pop(0)                                                # Remove the draw numbers and a blank line from the list
lines.pop(0)

number_of_cards = int((len(lines)+1) / 6)
cards = numpy.full((number_of_cards, 5, 5), -1, dtype=int)  # Create a 3D array for the cards

card_index=0
row_index=0
for line in lines:                                          # Fill the array of cards
    row=line.split()
    if len(row) != 0:
        cards[card_index][row_index]=row
        row_index+=1
    else:
        card_index += 1
        row_index=0

found=False
for draw_number in draw_numbers:                            # One by one replace the draw number on the cards with -1
    card_index=0
    for card in cards:
        if found == False:
            row_index=0
            for row in card:
                column_index=0
                for number in row:
                    if number == int(draw_number):
                        cards[card_index][row_index][column_index] = -1
                    column_index+=1
                row_index+=1
            sum_x = numpy.sum(card, axis=0)                     # After removing the number from the card check for a completed line.
            sum_y = numpy.sum(card, axis=1)                     # A completed line would count up to -5
            row_complete=numpy.where(sum_x == -5)
            column_complete=numpy.where(sum_y == -5)
            if len(row_complete[0])+len(column_complete[0]) >= 1:  # We have a winner!
                found=True
                card_total=0
                for row in card:
                    for number in row:
                        if number != -1:
                            card_total+=number
                print("Winning card:\n")
                print(card)
                print("Card Total: " + str(card_total))
                print("Last drawn number: " + str(draw_number))
                print("Puzzle solution: " + str(card_total * int(draw_number)))
                break
            card_index+=1