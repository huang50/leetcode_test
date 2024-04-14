from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 0:
            for i in range(k):
                tmp = nums[-1]
                nums.pop()
                nums.insert(0, tmp)
                