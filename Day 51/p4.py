def sum_of_unique(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return sum(num for num in count if count[num] == 1)

print(sum_of_unique([1, 2, 2, 3, 4, 4, 5]))