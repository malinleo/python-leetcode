from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Iterate over `colors` and `neededTime` with the same pointer
        # for each pair of same-colored balloons we remove the one with lower cost
        i = 1
        prev_i = 0
        total_time = 0
        colors_len = len(colors)
        while i < colors_len:
            prev_color, prev_cost = colors[prev_i], neededTime[prev_i]
            color, cost = colors[i], neededTime[i]
            if color == prev_color:
                if cost > prev_cost:
                    total_time += prev_cost
                    prev_i = i
                else:
                    total_time += cost
            else:
                prev_i = i
            i += 1
        return total_time


sol = Solution()
res = sol.minCost("aaaaaaaaaaaaaa", [1, 3, 6, 5, 4, 5, 4, 4, 2, 8, 3, 10, 6, 6])
print(res)
