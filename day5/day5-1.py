import math

def findRow(currentRange, halfs):
    if halfs[0] == 'F' or halfs[0] == 'L':
        newRange = [currentRange[0], math.floor((currentRange[1]-currentRange[0])/2) + currentRange[0]]
    else:
        newRange = [math.ceil((currentRange[1]-currentRange[0])/2) + currentRange[0], currentRange[1]]
    if len(halfs) == 1:
        return newRange
    else:
        return (findRow(newRange, halfs[1:]))
    
highest = 0
with open('advent2020/day5/day5input.txt', 'r') as file:
    for line in file.readlines():
        currentSeatId = (findRow([0,127],line[:7])[0] * 8 + findRow([0,7], line[7:])[0])
        if currentSeatId > highest:
            highest = currentSeatId
print('highest', highest)