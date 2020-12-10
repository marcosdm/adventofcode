# Reading the passwords
f = open("e:/Users/Marcos Diaz/Software/GitHub/AdventCode/2020/inputs/Day2_input.txt", "r")

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