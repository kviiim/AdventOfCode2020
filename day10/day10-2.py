valid = 0
nums = [0]
with open('advent2020/day10/day10input.txt', 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

nums.sort()
nums.append(nums[-1]+3)
threes = [0]
print(nums)

for numIndex in range(1,len(nums)):
    diff = nums[numIndex] - nums[numIndex-1]
    if diff == 3:
        threes.append(nums[numIndex])

def find_potentials(currentNum,endNum):
    global valid
    if (currentNum == endNum):
        return True
    if (currentNum + 1) in nums:
        if find_potentials(currentNum + 1,endNum) == True:
            valid += 1
    if (currentNum + 2) in nums:
        if find_potentials(currentNum + 2,endNum) == True:
            valid += 1
    if (currentNum + 3) in nums:
        if find_potentials(currentNum + 3,endNum) == True:
            valid += 1
    if not ((currentNum + 1) in nums and (currentNum + 2) in nums and (currentNum + 3) in nums):
        return False

totalValid = 1
for index in range(1,len(threes)):
    valid = 0
    find_potentials(threes[index - 1], threes[index])
    totalValid *= valid
    
print(totalValid)