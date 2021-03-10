class Solution:
    def lengthOfLongestSubstring(self, s):
        res = ''
        ln = 0
        for c in s:
            if c in res:
                res = res[res.index(c)+1:]
            res += c
            ln = max(len(res), ln)
        return ln


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('dvdf') == 3
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
    assert Solution().lengthOfLongestSubstring('aabaab!bb') == 3
    assert Solution().lengthOfLongestSubstring('asdasdasdfasd') == 4
