from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        row = bank[0]
        prev_sds_count = row.count("1")
        lasers_count = 0
        for row in bank[1:]:
            current_sds_count = row.count("1")
            if not current_sds_count:
                continue
            lasers_count += prev_sds_count * current_sds_count
            prev_sds_count = current_sds_count
        return lasers_count


sol = Solution()
kek = sol.numberOfBeams(["000", "111", "000"])
print(kek)
