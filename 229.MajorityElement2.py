class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alist = []
        blist = []
        anslist = []
        Len = len(nums)//3

        for i in range(0,len(nums)):
            if nums[i] not in alist:
                alist.append(nums[i])
                blist.append(1)
                if len(nums)<3:
                    anslist.append(nums[i])
            else:
                blist[alist.index(nums[i])] += 1
                if ((blist[alist.index(nums[i])] > len(nums)/3 )& 
                (nums[i] not in anslist)):
                    anslist.append(nums[i])

        return anslist
                     
print(Solution().majorityElement([0,0,0]))