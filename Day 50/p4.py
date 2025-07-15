from collections import deque

def first_non_repeating(s):
    queue = deque()
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
        queue.append(char)

        # Remove characters from front if they repeat
        while queue and freq[queue[0]] > 1:
            queue.popleft()

    if queue:
        return queue[0]
    else:
        return "No non-repeating character"


print(first_non_repeating("aabbcde"))  
print(first_non_repeating("aabb"))     
