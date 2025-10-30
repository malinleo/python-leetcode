from typing import List
import math


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        bit = 1
        while n > 0:
            if n & 1:
                powers.append(bit)
            bit <<= 1
            n >>= 1
        length = len(powers)
        lookup_table = [[0] * length for _ in range(length)]
        for idx, power in enumerate(powers):
            # Set first value for power
            lookup_table[idx][idx] = power
            # Make products and set it's values
            for length_idx in range(idx + 1, length):
                lookup_table[idx][length_idx] = (
                    lookup_table[idx][length_idx - 1] * powers[length_idx] % (10**9 + 7)
                )

        return [lookup_table[left][right] for left, right in queries]
