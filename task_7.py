class Solution:  # beats almost 95% by time lol
    def reverse(self, x: int) -> int:
        str_repr = str(x)
        is_negative = False
        if str_repr.startswith("-"):
            str_repr = str_repr[1:]
            is_negative = True
        start = "-" if is_negative else ""
        result = int(start + str_repr[::-1])
        if result > 2**31 - 1 or result < -(2**31):
            return 0
        return result


class Solution2:  # beats the same 95% by time + 83% by memory
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        digits = []
        while x:
            digits.append(x % 10)
            x = x // 10
        for idx, digit in enumerate(digits, 1):
            x += 10 ** (len(digits) - idx) * digit
        if x > 2**31 - 1 or x < -(2**31):
            return 0
        return -x if is_negative else x
