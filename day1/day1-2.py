input = open("advent2020/day1/day1input.txt","r")
nums = input.readlines()
for num1 in nums:
    num1int = int(num1.strip('\n'))
    for num2 in nums:
        num2int = int(num2.strip('\n'))
        for num3 in nums:
            num3int = int(num3.strip('\n'))
            if num1 != num2 and num1 != num3:
                if (num1int + num2int + num3int) == 2020:
                    print(num1int*num2int*num3int)
