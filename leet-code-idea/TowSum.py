__author__ = 'vivian'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = {};
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            if nums[i] in left:
                return [left[nums[i]], i]
            else:
                left[target - nums[i]] = i




if __name__ == '__main__' :
    nums = [3,2,4]
    target = 6
    Solution().twoSum(nums, target);