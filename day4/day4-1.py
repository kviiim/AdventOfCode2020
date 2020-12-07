numPass = 0
with open('advent2020/day4/day4input.txt', 'r') as file:
    currentPassword = ''
    for line in file.readlines():
        if len(line) == 1:
            #test password
            passwordComponents = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            if all(x in currentPassword for x in passwordComponents):
                numPass += 1
            currentPassword = ''
        else:
            currentPassword += (' ' + line.strip("\n"))
print(numPass)
