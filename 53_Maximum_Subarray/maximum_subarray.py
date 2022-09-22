"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""

from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -math.inf
        cur_sum = 0

        for x in nums:
            cur_sum = max(cur_sum + x, x)
            max_sum = max(max_sum, cur_sum)

        return max_sum


if __name__ == '__main__':
    sol = Solution().maxSubArray

    assert sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol([1]) == 1
    assert sol([5, 4, -1, 7, 8]) == 23
