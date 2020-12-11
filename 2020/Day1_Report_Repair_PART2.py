import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day1_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

myList = [int(x.rstrip("\n")) for x in f.readlines()]

for i in range(len(myList)):
    num1 = myList[i]
    for k in range(len(myList)-(i+1)):
        num2 = myList[i+k]
        for j in myList[i+k+1:]:
            num3 = j
            if num1+num2+num3==2020:
                print(num1,num2,num3, "  Result:", num1*num2*num3)

f.close()