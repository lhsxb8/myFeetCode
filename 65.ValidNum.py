class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'e' not in s:
            try:
                temp = float(s)
                return True
            except ValueError:
                return False
        
        elif 'e' in s:
            ind = s.index('e')
            str1 = s[:ind]
            if str1 == '':
                return False
            i = 0
            while str1[i] == ' ' and i+1<len(str1):
                i += 1
            str1 = str1[i:ind]
            if ' ' in str1 or str1 == '':
                return False
            str2 = s[ind+1:]
            try:
                temp1 = float(str1)
                temp2 = int(str2)
                return True
            except ValueError:
                return False

print(Solution().isNumber('           9e'))