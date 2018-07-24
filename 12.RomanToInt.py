class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        anslist = []
        ans = ""
        for i in range(5):
            anslist.append([])
        Len = len(str(num))
        ii = 1
        while num > 0:
            temp = num % 10
            if ii == 1:
                if temp == 4:
                    anslist[ii].append('IV')
                elif temp == 9:
                    anslist[ii].append('IX')
                elif temp < 5:
                    for k in range(temp):
                        anslist[ii].append('I')
                elif temp >= 5:
                    anslist[ii].append('V')
                    for k in range(temp - 5):
                        anslist[ii].append('I')
            
            if ii == 2:
                if temp == 4:
                    anslist[ii].append('XL')
                elif temp == 9:
                    anslist[ii].append('XC')
                elif temp < 5:
                    for k in range(temp):
                        anslist[ii].append('X')
                elif temp >= 5:
                    anslist[ii].append('L')
                    for k in range(temp - 5):
                        anslist[ii].append('X')

            if ii == 3:
                if temp == 4:
                    anslist[ii].append('CD')
                elif temp == 9:
                    anslist[ii].append('CM')
                elif temp < 5:
                    for k in range(temp):
                        anslist[ii].append('C')
                elif temp >= 5:
                    anslist[ii].append('D')
                    for k in range(temp - 5):
                        anslist[ii].append('C')

            if ii == 4:
                for k in range(temp):
                    anslist[ii].append('M')
            
            num = num // 10
            ii += 1
        for i in range(4,0,-1):
            if anslist[i] == []:
                continue
            else:
                for k in anslist[i]:
                    ans += k
        return ans

#print(Solution().intToRoman(58))
            
            
