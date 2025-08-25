from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)
    
    for word in strs:
        sorted_word_tuple = tuple(sorted(word))
        anagram_groups[sorted_word_tuple].append(word)
        
    return list(anagram_groups.values())


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output1 = group_anagrams(strs1)
print(f"Input: {strs1}")
print(f"Output: {output1}")


print("-" * 20)

strs2 = [""]
output2 = group_anagrams(strs2)
print(f"Input: {strs2}")
print(f"Output: {output2}")


print("-" * 20)

strs3 = ["a"]
output3 = group_anagrams(strs3)
print(f"Input: {strs3}")
print(f"Output: {output3}")
