from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(1, n):
            other = n - num
            if "0" not in str(other) and "0" not in str(num):
                return [num, other]s

    def _has_0_in_repr(self, number: int):
        while number:
            if not number % 10:
                return True
            number = number // 10
        return False


kek = Solution()
print(kek.getNoZeroIntegers(2))
