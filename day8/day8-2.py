with open('advent2020/day8/day8input.txt', 'r') as file:
    actualRules = file.readlines()

testFlip = 0

while testFlip < len(actualRules):
    if(actualRules[testFlip].split(' ')[0] == 'acc'):
        testFlip += 1
    else:
        doneNumbers = []
        accValue = 0
        ruleNum = 0
        rules = actualRules.copy()
        if rules[testFlip].split(' ')[0] == 'nop':
            rules[testFlip] = rules[testFlip].replace('nop', 'jmp')
        else:
            rules[testFlip] = rules[testFlip].replace('jmp', 'nop')
        fail = False
        while ruleNum in range(len(actualRules)) and fail == False:
            rule = rules[ruleNum]
            doneNumbers.append(ruleNum)
            splitRule = rule.split(' ')
            if splitRule[0] == 'acc':
                accValue += int(splitRule[1])
                ruleNum += 1
            elif splitRule[0] == 'jmp':
                ruleNum += int(splitRule[1])
            else:
                ruleNum += 1
            if ruleNum in doneNumbers:
                fail = True
        if (fail == False):
            print(accValue) 
            exit(0)
        testFlip += 1
   