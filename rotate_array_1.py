class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums_2 = nums[:]
        for i in range(length):
            nums[i] = nums_2[(i - k + length) % length]
