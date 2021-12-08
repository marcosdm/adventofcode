import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day2_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

horizontal=0
depth=0
aim=0

for i in f.readlines():
    movement,distance=i.split(" ")
    if movement=='forward':
        horizontal=horizontal+int(distance)
        depth=depth+(aim*int(distance))
    elif movement=='down':
        #depth=depth+int(distance)
        aim=aim+int(distance)
    else:
        #depth=depth-int(distance)
        aim=aim-int(distance)

print(horizontal*depth)

f.close()