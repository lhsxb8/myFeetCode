class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 1:
            return ["()"]
        anslist = []
        if n > 1:
            for a in self.generateParenthesis(n-1):
                indit_1 = a + "()"
                indit_2 = "()" + a
                indit_3 = "(" + a + ")"
                anslist.append(indit_1)
                anslist.append(indit_2) 
                anslist.append(indit_3)

        return list(set(anslist))

print(Solution().generateParenthesis(4))

            
            
            

        
        