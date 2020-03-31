class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            num = nums.pop(0)
            if (num!=val):
                nums.append(num)
        
        return len(nums)

sol = Solution()
print(sol.removeElement([3,2,2,3],3))
print(sol.removeElement([0,1,2,2,3,0,4,2],2))