from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return 0.0


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([2], []) == 2.0
