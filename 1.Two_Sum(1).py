class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums):
            for j in range(i + 1, len(nums)):
                if target == nums[i]+nums[j]:
                    return (i,j)

#print(Solution().twoSum([2, 7, 11, 15],9))                    
                
