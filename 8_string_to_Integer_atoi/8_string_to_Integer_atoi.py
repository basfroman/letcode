# Medium
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is
# either. This determines if the final result is negative or positive respectively. Assume the result is positive if
# neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the
# string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in
# the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should
# be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip(' ')
        if not len(s):
            return 0

        tmp = ''
        start = ''
        if s[0] in '-+' and len(s) > 1 and s[1].isdigit():
            start = s[0]
            s = s[1:]

        for i in s:
            if not i.isdigit():
                break
            else:
                tmp += i

        num = int(start + tmp if len(start + tmp) else '0')

        if not (-2 ** 31 < num < (2 ** 31)):
            return -2 ** 31 if num < 0 else (2 ** 31) - 1
        else:
            return num


if __name__ == '__main__':
    sol = Solution()
    assert sol.myAtoi('  -42') == -42
    assert sol.myAtoi(' - 31') == 0
    assert sol.myAtoi('qwe 12') == 0
    assert sol.myAtoi("-91283472332") == -2147483648
    assert sol.myAtoi('1w2') == 1
    assert sol.myAtoi('+-12') == 0
