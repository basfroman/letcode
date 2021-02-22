from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        if len(merged) % 2:
            # median = sum(merged)/len(merged)
            median = float(merged[int(len(merged) / 2)])
            return median
        else:
            lst = sorted(merged)
            half = int(len(lst)/2)

            l_lst = lst[:half][-1] if len(lst[:half]) > 0 else 0
            r_lst = lst[half:][0] if len(lst[half:]) > 0 else 0

            median = (l_lst + r_lst) / 2
            return median


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert sol.findMedianSortedArrays([1, 3], [2, 7]) == 2.5
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([2], []) == 2.0
    assert sol.findMedianSortedArrays([3], [-2, -1]) == -1.0
