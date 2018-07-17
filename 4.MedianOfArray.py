class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        Len1 = len(nums1)
        Len2 = len(nums2)
        LenTotal = Len1 + Len2

        alist = []
        while(len(nums1) and len(nums2)):
            if nums1[0] < nums2[0]:
                alist.append(nums1.pop(0))
            else:
                alist.append(nums2.pop(0))
            
        if nums1:
            alist += nums1
            
        else:
            alist += nums2
            
        if(LenTotal % 2 == 0):
            half = LenTotal//2
            return (alist[half-1]+alist[half])/2.0

        else:
            return float(alist[LenTotal//2])
