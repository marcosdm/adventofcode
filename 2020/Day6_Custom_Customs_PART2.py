import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day6_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

passengerCounter=0
answers=''
ansList=[]
group=[]

totalCounter=0
counter=0
prevL=''

# Data preparation
# Adding the...
for i in f.readlines():
    if i.rstrip("\n")=="":
        group.insert(0,passengerCounter)
        group.insert(1,''.join(sorted(answers)))
        ansList.append(group)
        group=[]
        passengerCounter=0
        answers=''
    else:
        passengerCounter=passengerCounter+1
        answers=answers+(i.rstrip("\n"))
#!! I need to think another solution or use another kind of loop. It's ugly
group.insert(0,passengerCounter)
group.insert(1,''.join(sorted(answers)))
ansList.append(group)

# Data analysis
for i in range(len(ansList)):
    for w in ansList[i][1]:
        if ansList[i][0]==1:
            totalCounter=totalCounter+1
        if prevL==w:
            counter=counter+1
            if counter==ansList[i][0]:
                totalCounter=totalCounter+1
        else:
            counter=1
            prevL=w
    print(ansList[i])
    print(totalCounter)

print("Number of equal answers per group: ", totalCounter)