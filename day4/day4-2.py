def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
numPass = 0
with open('advent2020/day4/day4input.txt', 'r') as file:
    currentPassword = ''
    lines = file.readlines()
    for lineNum in range(len(lines) + 1):
        try:
            line = lines[lineNum] 
        except:
            line = ' '
        if len(line) == 1:
            #test password
            passwordComponents = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            if all(x in currentPassword for x in passwordComponents):
                validPassword = True
                for component in currentPassword.split(' '):
                    if component:
                        [compType, compValue] = component.split(':')
                        if compType == 'byr':
                            if not (int(compValue) >= 1920 and int(compValue) <= 2002):
                                validPassword = False
                        elif compType == 'iyr':
                            if not (int(compValue) >= 2010 and int(compValue) <= 2020):
                                validPassword = False
                        elif compType == 'eyr':
                            if not (int(compValue) >= 2020 and int(compValue) <= 2030):
                                validPassword = False
                        elif compType == 'hgt':
                            if 'cm' in compValue :
                                height = compValue.strip('cm')
                                if not (isInt(height) and int(height) >= 150 and int(height) <= 193):
                                    validPassword = False
                            elif 'in' in compValue:
                                height = compValue.strip('in')
                                if not (isInt(height) and (int(height) >= 59 and int(height) <= 76)):
                                    validPassword = False
                            else:
                                validPassword = False
                        elif compType == 'hcl':
                            if not (len(compValue) == 7 and compValue[0] == '#' and all(x in '0123456789abcdef' for x in compValue.strip('#'))):
                                validPassword = False
                        elif compType == 'ecl' and not ( len(compValue) == 3 and any(x in compValue for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
                            validPassword = False
                        elif compType == 'pid':
                            if not (len(compValue) == 9 and isInt(compValue)):
                                validPassword = False
                if validPassword == True:
                    numPass += 1      
            currentPassword = ''
        else:
            currentPassword += (' ' + line.strip("\n"))
print(numPass)