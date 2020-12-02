totalValidPasswords = 0
with open('advent2020/day2/day2input.txt', 'r') as file:
    for testPassword in file.readlines():
        rangeAndLetter = testPassword.split(':')[0]
        letter = rangeAndLetter[-1]
        min = int(rangeAndLetter.split('-')[0])
        max = int(rangeAndLetter.split('-')[1].strip(letter))
        lettersInPassword = testPassword.count(letter) - 1
        if lettersInPassword <= max and lettersInPassword >= min:
            totalValidPasswords += 1
print (totalValidPasswords)
        