class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag_word_letters: list[list[str]] = [[] for _ in range(numRows)]
        going_down = True
        len_rows = numRows - 1
        current_row_counter = len_rows
        for letter in s:
            if current_row_counter >= 0 and going_down:
                # Going down in zigzag
                current_row_idx = len_rows - current_row_counter
                zigzag_word_letters[current_row_idx].append(letter)
                current_row_counter -= 1
                continue
            # Going up
            if current_row_counter == -1:
                current_row_counter = 1
                going_down = False
            current_row_idx = len_rows - current_row_counter
            zigzag_word_letters[current_row_idx].append(letter)
            if current_row_counter < len_rows - 1:
                current_row_counter += 1
            else:
                if current_row_counter == len_rows:
                    current_row_counter = len_rows - 1
                else:
                    current_row_counter = len_rows
                going_down = True
        result: list[str] = []
        for row in zigzag_word_letters:
            for letter in row:
                result.append(letter)
        return "".join(result)


sol = Solution()
res = sol.convert("PAYPALISHIRING", 2)
print(res)
