class Solution(object):
    def nextPermutation(self, nums):
        for k in range(len(nums)-1, -1, -1):
            if (k==0):
                nums.reverse()
                return nums
            if (nums[k-1]<nums[k]):
                break
        
        print('k = {k}')
        num = nums[k-1]
        nums[k-1] = nums[len(nums)-1]
        nums[len(nums)-1] = num

        if ( k==(len(nums)-1) ):
            return nums

        for i in range(len(nums)-1, k-1, -1):
            if (nums[i]<nums[i-1]):
                num = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = num
        
        return nums     

sol = Solution()
print(sol.nextPermutation([1,1,5]))