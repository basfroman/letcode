# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        if -2 ** 31 < result < 2 ** 31:
            return result
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(120) == 21
    assert sol.reverse(-21) == -12
    assert sol.reverse(0) == 0
    assert sol.reverse(1534236469) == 0
