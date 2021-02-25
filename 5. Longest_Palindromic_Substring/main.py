# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        temp = ''

        if not s:
            return ''

        for i in range(len(s)):
            temp += s[i]
            print(temp)


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestPalindrome('babad') == 'bab'
    assert sol.longestPalindrome('cbbd') == 'bb'
    assert sol.longestPalindrome('a') == 'a'
    assert sol.longestPalindrome('ac') == 'a'
 