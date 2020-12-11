import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day2_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

counter=0

for i in f.readlines():
        policy, password = i.rstrip("\n").split(":")
        minmax, word = policy.split(" ")
        pos1, pos2 = minmax.split("-")
        if password[int(pos1)]==word or password[int(pos2)]==word:
            if password[int(pos1)]==word and password[int(pos2)]==word:
                counter = counter
            else:
                counter = counter+1

print(counter)