class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        m = round( (l+r)/2 )
        while( (m!=l) and (m!=r) ):
            if (nums[m]>=nums[l]):
                l = m
            else:
                r = m
            m = round( (l+r)/2 )

        if (nums[r]<nums[l]):
            m = r
        else:
            m = l
        #print(f'l,m,r={l},{m},{r} nums[{m}]={nums[m]}')

        if (nums[m]==target):
            return m

        if (nums[m]>target):
            r = m
            l = 0
        else:
            l = m
            r = len(nums)-1
        
        while( (m!=l) and (m!=r) ):
            if (nums[m]==target):
                return m

            if (nums[m]<target):
                l = m
            else:
                r = m
            m = round( (l+r)/2 )
        
        if (nums[l]==target):
            return l
        elif (nums[r]==target):
            return r
        else:
            return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 3))