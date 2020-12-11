import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day1_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

myList = [int(x.rstrip("\n")) for x in f.readlines()]

for i in range(len(myList)):
    num1 = myList[i]
    for j in myList[i+1:]:
        num2 = j
        if num1+num2==2020:
            print(num1,num2, "  Result:", num1*num2)

f.close()