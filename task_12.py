class Solution:
    def intToRoman(self, num: int) -> str:
        conv_table = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        conv_digits = (1, 5, 10, 50, 100, 500, 1000)
        sub_form_digit = {4, 9}
        parts = []
        i = 0
        current_part = num % 10
        while num:
            parts.append(current_part)
            i += 1
            num //= 10
            current_part = num % 10 * 10**i
        result = []
        i -= 1
        for part in reversed(parts):
            if part != 0:
                closest_digit = 0
                diff = -1
                j = len(conv_digits)
                while diff < 0:
                    j -= 1
                    diff = part - conv_digits[j]
                    closest_digit = conv_digits[j]

                # Difference < 10 ** current iteration means that it is close enough to make it a subtractive form
                # F.e. part 400, diff with next number 500 is 100, means we should repr it as `CD`, not `CCCC`
                first_digit = part // 10**i
                if j < len(conv_digits) - 1 and first_digit in sub_form_digit:
                    next_closest_digit = conv_digits[j + 1]
                    if first_digit == 4:
                        result.append(
                            conv_table[closest_digit] + conv_table[next_closest_digit]
                        )
                    else:
                        prev_closest_digit = conv_digits[j - 1]
                        result.append(
                            conv_table[prev_closest_digit]
                            + conv_table[next_closest_digit]
                        )
                else:
                    while part > 0:
                        if part < closest_digit:
                            j -= 1
                            closest_digit = conv_digits[j]
                        result.append(conv_table[closest_digit])
                        part -= closest_digit
            i -= 1
        return "".join(result)


sol = Solution()
res = sol.intToRoman(4)
print(res)
