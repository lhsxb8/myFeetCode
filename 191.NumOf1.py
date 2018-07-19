class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        a = bin(n)
        for i in range(0,len(a)):
            if a[i] == '1':
                ans += 1
        return ans
                