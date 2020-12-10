
# Reading the report
f = open("e:/Users/Marcos Diaz/Software/Python/Advent_Code/2020/input.txt", "r")

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