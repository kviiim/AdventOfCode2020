totalValidPasswords = 0
with open('advent2020/day2/day2input.txt', 'r') as file:
    for testPassword in file.readlines():
        rangeAndLetter = testPassword.split(':')[0]
        letter = rangeAndLetter[-1]
        num1 = int(rangeAndLetter.split('-')[0])
        num2 = int(rangeAndLetter.split('-')[1].strip(letter))
        password = testPassword.split(':')[1]
        if (password[num1] == letter and password[num2] != letter) or (password[num2] == letter and password[num1] != letter):
            totalValidPasswords += 1
print (totalValidPasswords)
        