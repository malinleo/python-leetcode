from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
                if len(result) == 2:
                    return result
            seen.add(num)
        return result
