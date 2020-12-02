input = open("advent2020/day1input.txt","r")
nums = input.readlines()
for num1 in nums:
    num1int = int(num1.strip('\n'))
    for num2 in nums:
        num2int = int(num2.strip('\n'))
        if num1 != num2:
            if (num1int + num2int) == 2020:
                print(num1int*num2int)
