badNum = 1212510616
nums = []

with open('advent2020/day9/day9input.txt', 'r') as file:
    for line in file:
        if int(line.strip()) < badNum:
            nums.append(int(line.strip()))

for numIndex in range(len(nums)):
    testTotal = nums[numIndex]
    addedNums = [testTotal]
    subIndex = numIndex + 1
    while testTotal < badNum:
        testTotal += nums[subIndex]
        addedNums.append(nums[subIndex])
        subIndex += 1
    if testTotal == badNum:
        print(min(addedNums) + max(addedNums))
        break