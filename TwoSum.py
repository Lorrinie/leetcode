class Solution:
    def twoSum(self, nums, target):
        """
        return indices of two numbers in nums such that they add up to the target
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        checkedNumber = {}
        i = 0

        while i < len(nums):
            if (target - nums[i]) in checkedNumber.keys():
                return [checkedNumber[target - nums[i]], i]
            checkedNumber[nums[i]] = i
            i += 1
        return None

