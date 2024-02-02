# You are given an integer array `nums` of size `n` and a positive integer `k`.
#
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
#
# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to `k`.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array.
# And if there are multiple answers, return any of them.


class Solution:
    def divideArray(self, nums, k):
        length = len(nums)
        nums.sort()
        res = []
        for i in range(0, length, 3):
            if i + 2 < length and nums[i + 2] - nums[i] <= k:
                res.append(nums[i: i + 3])
            else:
                return []
        return res


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 3, 3, 2, 7, 3]
    k = 3
    expected = []
    assert sol.divideArray(nums, k) == expected

    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 2
    expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
    assert sol.divideArray(nums, k) == expected
