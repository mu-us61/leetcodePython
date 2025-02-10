# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# 1945. Sum of Digits of String After Convert

class Solution:
    @staticmethod
    def convert_char_to_str(char):
        # Convert character to its position in the alphabet and then to a numeric string
        return str(ord(char) - 96)

    @staticmethod
    def sum_of_digits(num):
        # Sum the digits of the given number
        return sum(int(digit) for digit in str(num))

    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert each character to its position and concatenate them
        numeric_str = ''.join(self.convert_char_to_str(char) for char in s)

        # Step 2: Convert the concatenated string to an integer
        total = int(numeric_str)

        # Step 3: Transform the total by summing its digits, repeat k times
        for _ in range(k):
            total = self.sum_of_digits(total)

        return total
