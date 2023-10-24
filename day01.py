from aoc import single_int_line as get_nums

def part_1(nums):
    for outer in range(0, len(nums)-1):
        for inner in range(1, len(nums)):
            if (nums[inner] + nums[outer]) == 2020:
                return nums[inner] * nums[outer]

def part_2(nums):
    for outer in range(0, len(nums)-2):
        for middle in range(1, len(nums)-1):
            for inner in range(2, len(nums)):
                if (nums[inner] + nums[middle] + nums[outer]) == 2020:
                    return nums[inner] * nums[middle] * nums[outer]

n = get_nums('input/day01.txt')
print("part_1: ", part_1(n))
print("part 2: ", part_2(n))
