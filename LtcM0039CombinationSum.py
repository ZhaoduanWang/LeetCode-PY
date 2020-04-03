class Solution(object):
    def combinationSum(self, candidates, target):
        dp = []
        res = []
        self.combinationSumHelper(0, candidates, target, dp, res)
        print(res)
        return res

    def combinationSumHelper(self, index, candidates, target, dp, res):
        if (target<=0):
            if (target==0):
                print(dp)                
                res.append(dp[:])
            return

        if (index<len(candidates)):
            value = candidates[index]
            dp.append(value)
            self.combinationSumHelper(index, candidates, target-value, dp, res)
            dp.pop()
            self.combinationSumHelper(index+1, candidates, target, dp, res)
            
sol = Solution()
sol.combinationSum([2,3,6,7], 7)
#sol.combinationSum([2,3,5], 8)