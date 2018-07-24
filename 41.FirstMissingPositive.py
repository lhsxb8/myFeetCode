class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newnums = []
        nums.sort()
        for i in nums:
            if i > 0 and i not in newnums:
                newnums.append(i)
        for i in range(len(newnums)):
            if newnums != i+1:
                return i+1