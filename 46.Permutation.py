class Solution:

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<=1):  
            return [nums]  
        anslist=[]  
        for i in range(len(nums)):  
            s=nums[:i]+nums[i+1:]  
            p=self.permute(s)  
            for x in p:  
                anslist.append(nums[i:i+1]+x)  
        return anslist

#print(Solution().permute([1,2,3]))
            


        