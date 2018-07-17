class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Num = 0
        for j in range(0,len(s)):
            ns = ''
            for i in s[j:]:
                if i not in ns:
                    ns = ns + i 
                    num = len(ns)
                else:
                    break
        
            if num > Num:
                Num = num
        return Num
