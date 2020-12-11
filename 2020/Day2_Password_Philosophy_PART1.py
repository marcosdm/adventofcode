import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day2_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

counter=0

for i in f.readlines():
        policy, password = i.rstrip("\n").split(":")
        minmax, word = policy.split(" ")
        minim, maxim = minmax.split("-")
        ocurrences = password.count(word)
        if int(minim)<=int(ocurrences)<=int(maxim):
            counter = counter+1

print(counter)