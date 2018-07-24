class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_Min = 0x80000000
        INT_Max = 0x7fffffff
        numstr = ""
        flag = True
        find = False
        for i in str:
            numi = ord(i)
            
            if i == ' ' and find == False:
                continue
            elif i == '-' and find == False:
                flag = False
                find = True
                continue
            elif i == '+' and find == False:
                flag = True
                find = True
            elif numi >47 and numi <58:
                numstr = numstr + i
                find = True
            else:
                break
        
        if numstr=='':
            ans = 0
        else:
            if flag == True:
                ans = int(numstr)
            else:
                ans = -int(numstr)
        if ans > INT_Max:
            return INT_Max
        elif ans < -INT_Min:
            return -INT_Min
        else:
            return ans
    
print(Solution().myAtoi("+1"))