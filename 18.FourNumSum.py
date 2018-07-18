class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ln = len(nums)
        res = set()
        adict = {}
        if ln < 4:
            return []

        nums.sort()
        for  p in range(ln):
            for q in range(p+1, ln):
                if nums[p] + nums[q] not in adict:
                    adict[nums[p] + nums[q]]=[(p, q)]
                else:
                    adict[nums[p] + nums[q]].append((p, q))
        for i in range(ln):
            for j in range(i+1, ln-2):
                temp = target - nums[i] - nums[j]
                if temp in adict:
                    for k in adict[temp]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]

#print(Solution().fourSum([1, 0, -1, 0, -2, 2],0))