class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ob1 = bin(x)[2:]
        ob2 = bin(y)[2:]
        ans = 0
        if len(ob1)<31:
            ob1 = "0"*(31-len(ob1)) + ob1
        if len(ob2)<31:
            ob2 = "0"*(31-len(ob2)) + ob2

        for i in range(31):
            if ob1[i]!=ob2[i]:
                ans += 1
        return ans

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                ans += self.hammingDistance(nums[i],nums[j])
        return ans

print(Solution().totalHammingDistance([4, 14, 2]))
