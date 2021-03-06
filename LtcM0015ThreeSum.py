class Solution(object):
    def threeSum(self, nums):
        rt = set()
        sortNums = nums.copy()
        sortNums.sort()

        for i in range(0, len(sortNums)-2):
            if ( (i==0) or (i>0 and sortNums[i]!=sortNums[i-1]) ):
                low = i+1
                high = len(sortNums)-1
                sum = 0-sortNums[i]

                while(low<high):
                    if ( (sortNums[low]+sortNums[high])==sum):
                        rt.add(tuple([sortNums[i], sortNums[low], sortNums[high]]))
                        while ( (low<high) and (sortNums[low]==sortNums[low+1]) ):
                            low += 1
                        while ( (low<high) and (sortNums[high]==sortNums[high-1]) ):
                            high -=  1
                        low += 1
                        high -= 1
                    elif ( (sortNums[low]+sortNums[high])>sum ):
                        high -= 1
                    else:
                        low += 1
        return rt

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))