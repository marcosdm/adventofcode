import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day5_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

identifierList=[]

#Function to identify the row on the plane given a boarding pass
def boardingPassRowChecker(boardingPass):
    minrow=0
    maxrow=127
    for i in range(len(boardingPass)-4):
        if boardingPass[i]=='F':
            maxrow=(maxrow+minrow)//2
        else:
            minrow=(minrow+maxrow+1)//2
    if boardingPass[6]=='B':
        return maxrow
    else:
        return minrow

#Function to identify the column on the plane given a boarding pass
def boardingPassColumnChecker(boardingPass):
    mincol=0
    maxcol=7
    for i in range(7,len(boardingPass)):
        if boardingPass[i]=='L':
            maxcol=(maxcol+mincol)//2
        else:
            mincol=(mincol+maxcol+1)//2
    if boardingPass[9]=='R':
        return maxcol
    else:
        return mincol

for i in f.readlines():
    identifier=boardingPassRowChecker(i)*8+boardingPassColumnChecker(i)
    identifierList.append(identifier)

print("Maximum identifier is: ",max(identifierList))



