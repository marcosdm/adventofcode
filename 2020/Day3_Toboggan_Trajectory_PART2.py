# Reading the passwords
f = open("e:/Users/Marcos Diaz/Software/Python/Advent_Code/2020/Day3_input.txt", "r")

#Create a list of lists
myList = [list(x.rstrip("\n")) for x in f.readlines()]

#Slopes
slope1=[1, 1]
slope2=[3, 1]
slope3=[5, 1]
slope4=[7, 1]
slope5=[1, 2]

def movements(slope):
    i=0
    j=0
    trees=0
    while i < len(myList):
        if myList[i][j%31] == "#":
            trees=trees+1
        i=i+slope[1]
        j=j+slope[0]
        print(i,j)
    return trees

result1=movements(slope1)
result2=movements(slope2)
result3=movements(slope3)
result4=movements(slope4)
result5=movements(slope5)

print("Number of trees SLOPE1: ", result1)
print("Number of trees SLOPE2: ", result2)
print("Number of trees SLOPE3: ", result3)
print("Number of trees SLOPE4: ", result4)
print("Number of trees SLOPE5: ", result5)

print("Total: ", result1*result2*result3*result4*result5)