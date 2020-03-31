class Solution(object):
    def searchRange(self, nums, target):
        l = 0; r = len(nums)-1; m = round( (l+r)/2 )

        while( (m!=l) and (m!=r) ):
            if (nums[m]==target):
                break
            if (nums[m]>target):
                r = m
            else:
                l = m
            m = round( (l+r)/2 )

        if (nums[m]!=target):
            return [-1,-1]

        l = m
        while (l>=0):
            if (nums[l]==target):
                l -= 1
            else:
                break
        l += 1
        
        r = m
        while ( r <= (len(nums)-1) ):
            if (nums[r]==target):
                r += 1
            else:
                break
        m += 1
        return [l, r]            

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))