total = 0
with open('advent2020/day6/day6input.txt', 'r') as file:
    currentGroupQuestions = ''
    firstInGroup = True
    for line in file:
        if len(line.strip()) == 0:
            total += len(currentGroupQuestions)
            currentGroupQuestions = ''
            firstInGroup = True
        else:
            if firstInGroup:
                currentGroupQuestions = line.strip()
                firstInGroup = False
            else:
                if currentGroupQuestions:
                    currentGroupQuestions = ''.join(set(line).intersection(currentGroupQuestions))
    total += len(currentGroupQuestions)
print(total)
