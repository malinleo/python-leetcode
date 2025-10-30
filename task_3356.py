from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # ideas:
        # 1. Remember all indexes where values are >0 and check only them
        # inside a loop, as well as subtract `val` only from these indexes if
        # they are between left and right
        # 2. Need to make it O(n) or O(n*logn) somehow
        non_zero_items_map = {idx: num for idx, num in enumerate(nums) if num > 0}
        if all((num <= 0 for num in non_zero_items_map.values())):
            return 0
        steps = 0
        for left, right, val in queries:
            valid_range = range(left, right + 1)
            for num_idx in non_zero_items_map.keys():
                if num_idx not in valid_range:
                    continue
                non_zero_items_map[num_idx] -= val

            non_zero_items_map = {
                idx: num for idx, num in non_zero_items_map.items() if num > 0
            }
            steps += 1
            if all((num <= 0 for num in non_zero_items_map.values())):
                return steps
        return -1
