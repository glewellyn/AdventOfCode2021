input = open('input.txt', 'r')                          # Read input file
input = input.readlines()

for i in reversed(range(len(input))):
    input[i]=input[i].replace('\n',"")                  # Remove newline characters
    clean=False
    while clean==False:                                 # Remove all complete chunks
        input[i]=input[i].replace("()","").replace("[]","").replace("{}","").replace("<>","")
        clean = True
        if input[i].find("()") >=0: clean=False
        if input[i].find("[]") >=0: clean=False
        if input[i].find("{}") >=0: clean=False
        if input[i].find("<>") >=0: clean=False
    for character in input[i]:
        if character in [")", "]", "}", ">"]:
            del input[i]
            break

autocomplete_scores=[]
for line in input:
    autocomplete_score=0
    for character in reversed(line):
        autocomplete_score *=5
        if character == "(":
            autocomplete_score+=1
        elif character == "[":
            autocomplete_score+=2
        elif character == "{":
            autocomplete_score+=3
        elif character == "<":
            autocomplete_score+=4
    autocomplete_scores.append(autocomplete_score)

autocomplete_scores.sort()
print(autocomplete_scores[int(len(autocomplete_scores)/2)])