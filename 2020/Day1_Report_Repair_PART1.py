
# Reading the report
f = open("e:/Users/Marcos Diaz/Software/GitHub/AdventCode/2020/inputs/Day1_input.txt", "r")

myList = [int(x.rstrip("\n")) for x in f.readlines()]

for i in range(len(myList)):
    num1 = myList[i]
    for j in myList[i+1:]:
        num2 = j
        if num1+num2==2020:
            print(num1,num2, "  Result:", num1*num2)

f.close()