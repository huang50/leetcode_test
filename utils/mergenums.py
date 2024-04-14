class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        tmp = nums1[0:m]
        i, j = 0, 0
        while i < m and j < n:
            if nums2[j] < tmp[i]:
                nums1[i + j] = nums2[j]
                j += 1

            else:
                nums1[i + j] = tmp[i]
                i += 1
        if i < m:
            nums1[i + j : :] = tmp[i::]
        elif j < n:
            nums1[i + j : :] = nums2[j::]
        print(nums1)

    def solution_back(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            if i == -1:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            elif j == -1:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1


if __name__ == "__main__":
    s = Solution()
    nums1, m, nums2, n = [1, 2, 3, 0, 0], 3, [0, 4, 5], 3
    s.solution_back(nums1, m, nums2, n)
