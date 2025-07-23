def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in num_set:  # start of a sequence
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)
    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
