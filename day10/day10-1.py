nums = [0]
with open('advent2020/day10/day10input.txt', 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

nums.sort()
nums.append(nums[-1]+3)

ones = 0
threes = 0

for numIndex in range(1,len(nums)):
    diff = nums[numIndex] - nums[numIndex-1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

print(ones, threes, ones*threes)