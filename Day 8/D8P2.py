input = open('input.txt', 'r')                  # Read input file
input = input.readlines()

for i in range(len(input)):                                                         # Place the signals and segments into a list
    input[i]=input[i].replace('\n',"").replace(" | "," ").split(" ")                # The first 10 places are the signals, the last 4 are segments

signals=[]                                                                          # Place signals and segments into two lists
segments=[]
for i in range(len(input)):
    signal=[]
    for j in range(10):
        signal.append(''.join(sorted(input[i][j])))
    signals.append(signal)
    segment=[]
    for j in range(10,14):
        segment.append(''.join(sorted(input[i][j])))
    segments.append(segment)

recognized_digits = [None] * 10

for signal in signals:                                                              # Every set of signals contains all 10 digits
    for digit in signal:                                                            # First find the uniquely identifiable numbers, 1,4,7 and 8
        if len(digit) == 2:                                                         # If lenth is 2, the represented number is 1
            recognized_digits[1] = digit
        elif len(digit) == 3:                                                       # If lenth is 3, the represented number is 7
            recognized_digits[7] = digit
        elif len(digit) == 4:                                                       # If lenth is 4, the represented number is 4
            recognized_digits[4] = digit
        elif len(digit) == 7:                                                       # If lenth is 7, the represented number is 8
            recognized_digits[8] = digit

    for digit in signal:                                                            # 6 is the only digit with 6 segments that doesn't have both segments used by digit 1
        if len(digit) == 6:
            if recognized_digits[1][0] not in digit or recognized_digits[1][1] not in digit:
                recognized_digits[6] = digit

    for digit in signal:                                                            # 3 is the only digit with 5 segments that has both segments used by digit 1
        if len(digit) == 5:
            if recognized_digits[1][0] in digit and recognized_digits[1][1] in digit:
                recognized_digits[3] = digit

    upper_left_segment=recognized_digits[4]                                         # By determining which letter corresponds to the upper left segment we can distinguish digits 2 and 5
    for letter in (recognized_digits[3]):
        upper_left_segment=upper_left_segment.replace(letter,"")

    for digit in signal:                                                            # 5 is the only digit with 5 segments that has the upper left segment on
        if len(digit) == 5:
            if upper_left_segment in digit:                                         # if the upper left segment is lit, it must be digit 5
                recognized_digits[5] = digit
            elif digit != recognized_digits[3]:                                     # If it has 5 segments and is not digits 5 or 3, it must be digit 2
                recognized_digits[2] = digit

    middle_segment=recognized_digits[4]                                             # Only 0 and 9 left to determine, distinguishable by the middle segment.
    for letter in (recognized_digits[1]):
        middle_segment=middle_segment.replace(letter,"")
    middle_segment=middle_segment.replace(upper_left_segment,"")

    for digit in signal:                                                            
        if len(digit) == 6 and digit != recognized_digits[6]:
            if middle_segment in digit:
                recognized_digits[9]=digit
            else :
                recognized_digits[0]=digit

    print(recognized_digits)

for segment in segments:
    number = ""
    for digit in segment:
        number += str(recognized_digits[i].index(digit))
    print(str(i) + " " + str(number))
    i+=1
