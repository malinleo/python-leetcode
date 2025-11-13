from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n == 0:
                continue
            if not stack or stack[-1] < n:
                res += 1
                stack.append(n)
        return res


a = [1, 2, 3, 2, 1, 2]
