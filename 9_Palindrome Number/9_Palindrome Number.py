# Easy
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome(121) == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(10) == False
    assert sol.isPalindrome(0) == True
