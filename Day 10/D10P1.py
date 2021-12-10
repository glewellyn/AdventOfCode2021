input = open('input.txt', 'r')                          # Read input file
input = input.readlines()

error_score=0

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

for line in input:
    for character in line:
        if character == ")":
            error_score+=3
            break
        elif character == "]":
            error_score+=57
            break
        elif character == "}":
            error_score+=1197
            break
        elif character == ">":
            error_score+=25137
            break
        

for line in input:
    print(line)
    
print(error_score)