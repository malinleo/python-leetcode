class Solution:
    def numSplits(self, s: str) -> int:
        good_splits_count = 0
        if not s:
            return good_splits_count
        left_split_letters_counter: dict[str, int] = {}
        right_split_letters_counter: dict[str, int] = {}

        # All letters are now in right split, so we count them all and store
        # results
        for letter in s:
            right_split_letters_counter.setdefault(letter, 0)
            right_split_letters_counter[letter] += 1

        for idx, letter in enumerate(s, 1):
            left, right = s[:idx], s[idx:]
            if not left or not right:
                continue

            # Add to left counter
            left_split_letters_counter.setdefault(letter, 0)
            left_split_letters_counter[letter] += 1

            # Remove from right counter
            right_split_letters_counter[letter] -= 1
            if right_split_letters_counter[letter] == 0:
                del right_split_letters_counter[letter]

            unique_letters_left = len(left_split_letters_counter)
            unique_letters_right = len(right_split_letters_counter)
            if unique_letters_left == unique_letters_right:
                good_splits_count += 1

        return good_splits_count
