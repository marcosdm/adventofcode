import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day3_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

#Create a list of lists
myList = [list(x.rstrip("\n")) for x in f.readlines()]

#Initiate position variables
i=0
j=0

#Initiate tree counter
trees=0

#Check the Toboggan trajectory
for i in range(len(myList)):
    #print("My position: ", i,j)
    if myList[i][j%31] == "#":
        trees=trees+1
    i=i+1
    j=j+3

print("Number of trees: ", trees)