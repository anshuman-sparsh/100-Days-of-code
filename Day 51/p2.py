def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None


print(second_largest([5, 1, 9, 3, 7]))
