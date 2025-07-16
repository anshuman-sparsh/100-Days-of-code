def find_majority(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num in count:
        if count[num] > len(nums) // 2:
            return num
    return "No majority element"

print(find_majority([1, 2, 3, 3, 2, 2, 2]))
print(find_majority([1, 2, 3, 4])) 