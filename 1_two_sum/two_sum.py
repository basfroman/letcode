# Easy
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


class Solution:

    # solution 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            if target == v * 2 and nums.count(v) > 1:
                return [i, nums.index(v, i + 1)]
            else:
                if nums.count(target - v) and i != nums.index(target - v):
                    return [i, nums.index(target - v)]


if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    assert Solution().twoSum([1, 2, 3, 4, 5], 8) == [2, 4]
    assert Solution().twoSum([2, 5, 5, 11], 10) == [1, 2]
    assert Solution().twoSum([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11) == [5, 11]
