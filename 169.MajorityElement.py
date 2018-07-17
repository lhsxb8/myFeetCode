class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alist = []
        blist = []
        Len = len(nums)//2
        temp = 0
        for i in range(0,len(nums)):
            if nums[i] not in alist:
                alist.append(nums[i])
                blist.append(1)
                temp += 1
            else:
                blist[alist.index(nums[i])] += 1
        
        for i in range(0,temp):
            if blist[i] > Len:
                return alist[i]
