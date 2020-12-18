import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day6_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

groupList=[]
group=''
totalAns=0

for i in f.readlines():
    if i.rstrip("\n")!="":
        group=group+i.rstrip("\n")
    else:
        groupList.append(group)
        group=''
groupList.append(group)

for i in range(len(groupList)):
    totalAns=totalAns+ len(set(groupList[i]))

print("Total unique answers: ", totalAns)