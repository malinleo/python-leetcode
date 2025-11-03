class Solution:
    def myAtoi(self, s: str) -> int:
        max_res = 2**31 - 1
        min_res = -(2**31)
        allowed_digits_str = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        s = s.lstrip(" ")
        is_negative = False
        if not s:
            return 0
        if s[0] in {"+", "-"}:
            is_negative = s[0] == "-"
            s = s[1:]
        digits = []
        for char in s:
            if char not in allowed_digits_str:
                break
            digit = int(char)
            if not digits and digit == 0:
                continue
            digits.append(digit)
        result = 0
        for idx, digit in enumerate(digits, 1):
            result += 10 ** (len(digits) - idx) * digit
        result = -result if is_negative else result
        if result > max_res:
            return max_res
        if result < min_res:
            return min_res
        return result


class Solution2:
    def myAtoi(self, s: str) -> int:
        max_res = 2**31 - 1
        min_res = -(2**31)
        allowed_digits_str = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        s = s.lstrip(" ")
        is_negative = False
        if len(s) == 0:
            return 0
        if s[0] in {"+", "-"}:
            is_negative = s[0] == "-"
            s = s[1:]
        digits = []
        for char in s:
            if char not in allowed_digits_str:
                break
            if len(digits) == 0 and char == "0":
                continue
            digits.append(char)
        result = int("".join(digits)) if digits else 0
        result = -result if is_negative else result
        if result > max_res:
            return max_res
        if result < min_res:
            return min_res
        return result
