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
        status = True
        for k,v in allPassports[p].items():
            if k == "byr":
                if len(v) == 4 and v[0:4].isdigit() and 1920<=int(v)<=2002:
                    status
                else:
                    status = False
            elif k == "iyr":
                if len(v) == 4 and v[0:4].isdigit() and 2010<=int(v)<=2020:
                    status
                else:
                    status = False
            elif k == "eyr":
                if len(v) == 4 and v[0:4].isdigit() and 2020<=int(v)<=2030:
                    status
                else:
                    status = False
            elif k == "hgt":
                if v.endswith("cm") and v[0:3].isdigit():
                    if 150<=int(v[0:3])<=193:
                        status
                    else:
                        status = False
                elif v.endswith("in") and v[0:2].isdigit():
                    if 59<=int(v[0:2])<=76:
                        status
                    else:
                        status = False
                else:
                    status = False
            elif k == "hcl":
                if v[0]=="#" and v[1:7].isalnum():
                    status
                else:
                    status = False
            elif k == "ecl":
                if v in ("amb","blu","brn","gry","grn","hzl","oth"):
                    status
                else:
                    status = False
            elif k == "pid":
                if len(v) == 9 and v.isdigit():
                    status
                else:
                    status = False   
        if status == True:
            validPassports = validPassports + 1
        else:
            notValidPassports = notValidPassports + 1
    else:
        notValidPassports = notValidPassports + 1

print("Number of valid passports: ", validPassports)
print("Number of not valid passports: ", notValidPassports)