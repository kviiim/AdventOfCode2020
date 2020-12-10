valid = 0
nums = [0]
with open('advent2020/day10/day10input.txt', 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

nums.sort()
nums.append(nums[-1]+3)

def find_potentials(currentNum):
    global valid
    if (currentNum == nums[-1]):
        return True
    if (currentNum + 1) in nums:
        if find_potentials(currentNum + 1) == True:
            valid += 1
    if (currentNum + 2) in nums:
        if find_potentials(currentNum + 2) == True:
            valid += 1
    if (currentNum + 3) in nums:
        if find_potentials(currentNum + 3) == True:
            valid += 1
    if not ((currentNum + 1) in nums and (currentNum + 2) in nums and (currentNum + 3) in nums):
        return False

find_potentials(nums[0])
print(valid)