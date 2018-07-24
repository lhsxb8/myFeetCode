class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        d = {'{': '}', '[': ']', '(': ')'}
        alist = []
        for i in s:
            if i in d:
                alist.append(i)
            else:
                if not alist or d[alist.pop()] != i:
                    return False

        return alist ==[]