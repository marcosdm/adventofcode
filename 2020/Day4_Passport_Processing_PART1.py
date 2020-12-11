import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "inputs/Day4_input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

allPassports = {}
passport={}
passportCounter=0
validPassports=0
notValidPassports=0

for i in f.readlines():
    if i.rstrip("\n")=="":
        passportCounter = passportCounter + 1
        passport={}
    else:
        for e in i.rstrip("\n").split(" "):
            passport[e.split(":")[0]]=e.split(":")[1]
        allPassports[passportCounter] = passport

# To know the number of passports - 288
print("Number of passports: ", len(allPassports.keys()))

for p in allPassports.keys():
    if all (k in allPassports[p] for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        validPassports = validPassports + 1
    else:
        notValidPassports = notValidPassports + 1

print("Number of valid passports: ", validPassports)
print("Number of not valid passports: ", notValidPassports)