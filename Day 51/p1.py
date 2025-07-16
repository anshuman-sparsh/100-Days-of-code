def find_all_missing(nums):

    if not nums:
        return []

    num_set = set(nums)
    missing_numbers = []
    
    start = min(nums)
    end = max(nums)
    
    for i in range(start, end + 1):
        if i not in num_set:
            missing_numbers.append(i) 
            
    return missing_numbers


print(find_all_missing([1, 2, 4, 6, 8]))