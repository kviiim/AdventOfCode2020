preambleLen = 25
nums = []

with open('advent2020/day9/day9input.txt', 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

for numIndex in range(preambleLen,len(nums)):
    works = False
    testNum = nums[numIndex]
    preamble = nums[(numIndex - preambleLen):numIndex]
    for num1 in preamble:
        if (testNum - num1) in preamble and (num1 * 2 != testNum):
            works = True
            break
    if(works == False):
        print(testNum)
        exit(0)  
