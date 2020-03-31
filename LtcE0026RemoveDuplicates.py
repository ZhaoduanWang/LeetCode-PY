class Solution(object):
    def removeDuplicates(self, nums):
        prev = nums[len(nums)-1]

        for i in range(len(nums)):
            num = nums.pop(0)
            if (num!=prev):
                nums.append(num)
                prev = num

        return len(nums)

sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))