from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        # 1. Iterate over nums with sliding window of length k
        # 2. On each iteration count all occurrences of the num in subarray i..i+k-1
        # 3. Get top x ocurrences
        # 4. Sum all of them and add to `answers`

        # Can we get top x without counter?

        answer = []
        i = 0
        while i + k - 1 != len(nums):
            counter = self.make_counter(nums[i : i + k])
            top = sorted(
                [(num, count) for num, count in counter.items()],
                key=lambda item: (-item[1], -item[0]),
            )
            answer.append(sum(item[0] * item[1] for item in top[:x]))
            i += 1
        return answer

    @staticmethod
    def make_counter(nums: List[int]):
        counter = {}
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1
        return counter
