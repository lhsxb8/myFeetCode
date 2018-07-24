class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<=1):  
            return [nums]  
        anslist=[]  
        for i in range(len(nums)):  
            s=nums[:i]+nums[i+1:]  
            p=self.permuteUnique(s)  
            for x in p:  
                if nums[i:i+1]+x not in anslist:
                    anslist.append(nums[i:i+1]+x)  
        return anslist



        