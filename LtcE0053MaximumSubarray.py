class Solution:
    def maxSubArray(self, nums) -> int :
        for i in range(len(nums)):
            if (i==0):
                maxSum = nums[0]
                curSum = nums[0]

            curSum += nums[i]
            if (curSum<nums[i]):
                curSum = nums[i]
            if curSum > maxSum:
                maxSum = curSum 
        
        return maxSum

sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))