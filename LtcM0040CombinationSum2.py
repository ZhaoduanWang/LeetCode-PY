class Solution(object):
    def combinationSum2(self, candidates, target):
        dp = []
        res = []
        self.combinationSum2Helper(0, candidates, target, dp, res)
        print(res)
        return res

    def combinationSum2Helper(self, index, candidates, target, dp, res):
        if (target<=0):
            if (target==0):
                print(dp)                
                res.append(dp[:])
            return

        if (index<len(candidates)):
            value = candidates[index]
            dp.append(value)
            self.combinationSum2Helper(index+1, candidates, target-value, dp, res)
            dp.pop()
            
sol = Solution()
sol.combinationSum2([10,1,2,7,6,1,5], 8)
#sol.combinationSum2([2,3,5], 8)