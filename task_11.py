from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i, line in enumerate(height):
            for j, other_line in enumerate(height[i + 1 :], start=i + 1):
                min_line = line if line < other_line else other_line
                distance = j - i
                area = min_line * distance
                if area > max_area:
                    max_area = area
        return max_area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = 0, 0
        max_area = 0
        while l != r:
            left_line = height[l]
            right_line = height[r]
            if left_line < max_left and right_line < max_right:
                l += 1
                r -= 1
                continue
            is_left_shorter = left_line < right_line
            min_line = left_line if is_left_shorter else right_line
            distance = r - l
            area = min_line * distance
            if area > max_area:
                max_area = area
            if is_left_shorter:
                l += 1
            else:
                r -= 1
        return max_area
