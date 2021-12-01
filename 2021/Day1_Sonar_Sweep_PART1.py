import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day1_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

myList = [int(x.rstrip("\n")) for x in f.readlines()]

inc=0

for i in range(len(myList)-1):
    num1 = myList[i]
    num2 = myList[i+1]
    if num1<num2:
        inc=inc+1

print("incrementos: ", inc)

f.close()