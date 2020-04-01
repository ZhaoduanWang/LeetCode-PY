class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)-1):
            if (nums[i]==target):
                return i
            if (i==0) and (nums[0]>target):
                return i                
            if (nums[i-1]<target) and (nums[i]>target):
                return i
        return len(nums)

sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))
print(sol.searchInsert([1, 3, 5, 6], 2))
print(sol.searchInsert([1, 3, 5, 6], 7))
print(sol.searchInsert([1, 3, 5, 6], 0)) 