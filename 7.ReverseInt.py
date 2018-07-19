class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        judge = True
        if x < 0:
            judge = False
            x = -x
            
        ans = x%10
        x = x//10
        
        while(x!=0):
            ans = ans * 10
            ans += x % 10
            x = x // 10
     
        if judge == False:
            ans = -ans
        if ans > 2147483647 or ans < -2147483648:
            return 0
        return ans
        