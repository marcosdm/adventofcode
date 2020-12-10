# Reading the passwords
f = open("e:/Users/Marcos Diaz/Software/Python/Advent_Code/2020/Day2_input.txt", "r")

counter=0

for i in f.readlines():
        policy, password = i.rstrip("\n").split(":")
        minmax, word = policy.split(" ")
        minim, maxim = minmax.split("-")
        ocurrences = password.count(word)
        if int(minim)<=int(ocurrences)<=int(maxim):
            counter = counter+1

print(counter)