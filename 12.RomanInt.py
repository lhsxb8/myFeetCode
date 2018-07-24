class Solution:
    def romanToInt(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = 0
        i = 0
        while i < (len(num)-1):
            if num[i] == 'I':
                if  num[i+1] == 'V':
                    i += 2
                    ans += 4
                elif num[i+1] == 'X':
                    i += 2
                    ans += 9
                else:
                    i += 1
                    ans += 1
            elif num[i] == 'V':
                i += 1
                ans += 5

            elif num[i] == 'X':
                if  num[i+1] == 'L':
                    i += 2
                    ans += 40
                elif num[i+1] == 'C':
                    i += 2
                    ans += 90
                else:
                    i += 1
                    ans += 10
            elif num[i] == 'L':
                i += 1
                ans += 50
            elif num[i] == 'C':
                if  num[i+1] == 'D':
                    i += 2
                    ans += 400
                elif num[i+1] == 'M':
                    i += 2
                    ans += 900
                else:
                    i += 1
                    ans += 100
            elif num[i] == 'D':
                i += 1
                ans += 500
            elif num[i] == 'M':
                i += 1
                ans += 1000
        
        if i > len(num)-1:
            return ans 
        if i == len(num)-1:
            if num[i] == 'I':
                return ans + 1
            elif num[i] == 'V':
                return ans + 5 
            elif num[i] == 'X':
                return ans + 10
            elif num[i] == 'L':
                return ans + 50
            elif num[i] == 'C':
                return ans + 100
            elif num[i] == 'D':
                return ans + 500
            elif num[i] == 'M':
                return ans + 1000


print(Solution().romanToInt('DCXXI'))