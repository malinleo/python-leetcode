class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # Can we prove that we can't go to 0 before looping?
        # # 1. if num2 > num1 + 1 we can't go to zero
        # if num2 > num1 + 1:
        #     return -1
        # # 2. if num2 == num1 + 1 we can go to zero in 1 step without calculations
        # if num2 == num1 + 1:
        #     return 1
        steps_count = 0
        lookup_list = [abs(2**i + num2) for i in range(0, 61)]
        lookup_list.sort()
        result = num1
        i = self._find_closest_number(
            result, len(lookup_list) // 2, result, lookup_list
        )
        results_cache = {num1}
        # If abs(result) >= some abs(item) that is closest to result in lookup list we can continue
        # If result == 0 we're done and return steps_count
        # If result is in loop we're done and return -1
        while result != 0 or self._check_loop(result, results_cache):
            result = num1 - (2**i - num2)
            # How to choose i correctly?
            i = self._find_closest_number(
                result, len(lookup_list) // 2, result, lookup_list
            )

    @classmethod
    def _check_loop(cls, result: int, results: set[int]) -> bool:
        return result not in results

    @classmethod
    def _find_closest_number(
        cls,
        least_diff_abs: int,
        middle: int,
        target: int,
        lookup_list: list[int],
    ) -> int:
        number = lookup_list[middle]
        current_diff = abs(target - number)
        if current_diff < least_diff_abs:
            least_diff_abs = current_diff
            lookup_list = lookup_list[middle:]
            middle = len(lookup_list) // 2 + middle
        else:
            lookup_list = lookup_list[:middle]
            middle = len(lookup_list) // 2

        if not lookup_list:
            return least_diff_abs
        return cls._find_closest_number(least_diff_abs, middle, target, lookup_list)
