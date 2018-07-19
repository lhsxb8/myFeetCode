class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftlist = []
        rightlist = []
        Len = len(height)
        i = 0
        ans = 0
        while(i<Len-1):
            k = 1
            while(height[i] > height[i + k]):
                if [i,height[i]] not in leftlist:
                    leftlist.append([i,height[i]])
                k += 1
                if i + k >= Len:
                    break
            
            if height[i+1] >= height[i]:
                #if [i+1,height[i+1]] not in leftlist:
                leftlist.append([i+1,height[i+1]])
                #if [i,height[i]] not in leftlist:
                leftlist.append([i,height[i]])
                k += 1

            i += k

        i = 0
        while(i<Len and i>=0):
            k = 1
            while(height[Len - i - 1] > height[Len - i - 1 - k]):
                if [Len-i-1,height[Len-i-1]] not in rightlist:
                    rightlist.append([Len-i-1,height[Len-i-1]])
                k += 1
                if Len - i - 1 - k <= -1:
                    break
            
            if height[Len - i -1] <= height[Len - i -2]:
                #if [Len-i-1,height[Len-i-1]] not in rightlist:
                rightlist.append([Len-i-1,height[Len-i-1]])
                #if [Len-i-2,height[Len-i-2]] not in rightlist:
                rightlist.append([Len-i-2,height[Len-i-2]])
                k += 1
            
            i += k
            
        leftlen = len(leftlist)
        rightlen = len(rightlist)

        for i in range(leftlen):
            for j in range(rightlen):
                temp = (rightlist[j][0] - leftlist[i][0])*min(rightlist[j][1],leftlist[i][1])
                if temp > ans:
                    ans = temp

        
        return ans

print(Solution().maxArea([1,2,3,4,5,6,7,8,9]))