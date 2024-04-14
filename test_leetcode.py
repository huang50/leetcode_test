import pytest
import sys
import os
sys.path.append('/code')
from utils import mergenums, rotatedarray

from typing import List
merge = mergenums.Solution()
rotate = rotatedarray.Solution()

class Test_LeetCode:
    @pytest.mark.parametrize("nums1, m, nums2, n, res", [([1, 2, 3, 0, 0], 3, [4, 5], 2, [1, 2, 3, 4, 5])])
    def test_merge_nums(self, nums1: List[int], m: int, nums2: List[int], n: int, res: List[int]) -> None:
        merge.merge(nums1, m, nums2, n)
        assert nums1 == res