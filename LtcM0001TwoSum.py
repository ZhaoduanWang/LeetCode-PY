class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, val in enumerate(nums):
            dif = target - val
            if (dif in map):
                return [i, map[dif]]
            else:
                map[val] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))