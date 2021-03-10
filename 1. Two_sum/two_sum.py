from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while True:
            num = nums[i]
            sec = target - num
            if nums.count(sec) and nums.index(sec) != i:
                return [i, nums.index(sec)]
            if nums.count(num) > 1:
                return [i, nums.index(num, i + 1)]
            i += 1


if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    assert Solution().twoSum([1, 2, 3, 4, 5], 8) == [2, 4]

