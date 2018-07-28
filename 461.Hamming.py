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
        return  ans

print(Solution().hammingDistance(1,4))
