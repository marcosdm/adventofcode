import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day3_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

myList = [(x.rstrip("\n")) for x in f.readlines()]

def rates_calc(myList, type):
    #Create an auxiliary array to hold the 1's counters for each position
    counters=[0]*len(myList[0])
    gamma=''
    epsilon=''

    #Go through the list to count the number of 1's for each position
    for i in range(len(myList)):
        for x, y in enumerate(myList[i]):
            if y == '1':
                counters[x]+=1
    
    #Calculate gamma and epsilon rates comparing counters with threshold
    for i in range(len(myList[0])):
        if counters[i] == len(myList)/2:
            gamma+='1'
            epsilon+='0'
        elif counters[i] > len(myList)/2:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'

    if type=='gamma':
        return gamma
    else:  
        return epsilon

#Recursive Function to remove elements
def remove_elements(secondList, type, pos):
    #End of list, return the last value.
    if len(secondList) == 1:
        return(secondList)
    
    #Calculate gamma and epsilon on each recursive iteration for remaining elements
    gamma=rates_calc(secondList, 'gamma')
    epsilon=rates_calc(secondList, 'epsilon')

    #Auxiliary list to store the selected elements for removing
    removed=[]

    #Go through the list to select the elements to remove and add those elements to the auxiliary list
    for elem in secondList:
        if type=='gamma':
            if elem[pos]!=gamma[pos]:
                removed.append(elem)
        else:
            if elem[pos]!=epsilon[pos]:
                removed.append(elem)
    
    #Save the list without elements removed
    secondList=set(secondList)-set(removed)
    #List updated and move forward
    return remove_elements(list(secondList), type, pos+1)

oxygen_rating = int(remove_elements(myList, 'gamma', 0).pop(), 2)
co2_rating = int(remove_elements(myList, 'epsilon', 0).pop(), 2)

print('Oxygen generator rating: ', oxygen_rating)
print('CO2 scrubber rating: ', co2_rating)

print('LIFE SUPPORT RATING: ', oxygen_rating*co2_rating)

f.close()