input = open('input.txt', 'r')                  # Read input file
input = input.readlines()

for i in range(len(input)):                                                     # Place the signals and segments into a list
    input[i]=input[i].replace('\n',"").replace(" | "," ").split(" ")            # The first 10 places are the signals, the last 4 are segments

signals=[]                                                                      # Place signals and segments into two lists
segments=[]
for i in range(len(input)):
    signal=[]
    for j in range(10):
        signal.append(input[i][j])
    signals.append(signal)
    segment=[]
    for j in range(10,14):
        segment.append(input[i][j])
    segments.append(segment)

recognized_number_count=0
for line in segments:
    for segment in line:
        if len(segment) in [2,3,4,7]:
            recognized_number_count+=1

print(recognized_number_count)