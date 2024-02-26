from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        counter = Counter(reversed(s))
        return ''.join(i for i in reversed(counter) if counter[i] == max(counter.values()))



if __name__ == '__main__':
    sol = Solution()

    s = "aabcbbca"
    assert sol.lastNonEmptyString(s) == 'ba'

    s = 'abcd'
    assert sol.lastNonEmptyString(s) == 'abcd'
