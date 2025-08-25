from typing import List

def max_area(height: List[int]) -> int:
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_water = max(max_water, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(height)
    print(f"Input: {height}")
    print(f"Output: {result}")