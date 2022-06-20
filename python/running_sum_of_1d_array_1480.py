class Solution:
    def runningSum(self, nums):
        return self.helper(nums, [], 0)
        
    
    def helper(self, nums, res, n):
        if n == 0:
            res.append(nums[0])
            n += 1
            return self.helper(nums, res, n)
        elif n >= len(nums):
            return res
        else:
            res.append(res[n-1] + nums[n])
            n += 1
            return self.helper(nums, res, n)


solution = Solution()
res = solution.runningSum([1,2,3,4])
print(res)