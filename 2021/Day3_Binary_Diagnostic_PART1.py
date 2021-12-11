import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day3_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

myList = [(x.rstrip("\n")) for x in f.readlines()]

counters=[0]*len(myList[0])
gamma=''
epsilon=''

for i in range(len(myList)):
    for x, y in enumerate(myList[i]):
        if y == '1':
            counters[x]+=1

for i in range(len(myList[0])):
    if counters[i] > len(myList)//2:
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'

print('Gamma rate: ', int(gamma, 2))
print('Epsilon rate: ', int(epsilon, 2))
print('Power consumption: ', int(gamma, 2)*int(epsilon, 2))

f.close()