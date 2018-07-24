class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Len = len(nums)
        for i in range(Len):
            
            if nums[i] >= target:
                return i 
            elif i == Len - 1:
                return Len