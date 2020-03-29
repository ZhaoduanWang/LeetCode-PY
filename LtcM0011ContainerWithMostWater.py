class Solution(object):
    def maxArea(self, height):
        l1 = 0
        r1 = 1
        max = r1-l1

        for r in range(2,len(height)):
            area = min(height[l1],height[r]) * (r-l1)
            if (area>max) :
                if ( (min(height[r1],height[r]) * (r-r1)) > area ) :
                    l1 = r1
                    max = min(height[r1],height[r]) * (r-r1)
                r1 = r
                max = area
        
        print(max)


sol = Solution()
sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])