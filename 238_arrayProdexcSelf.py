class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        preProduct = 1
        for i in range(1, len(nums), 1):
            preProduct *= nums[i - 1]
            res[i] *= preProduct

        postProduct = 1
        for j in range(len(nums) - 2, -1, -1):
            postProduct *= nums[j + 1]
            res[j] *= postProduct

        return res
    
nums = [1,2,3,4]
ans = [24,12,8,6]

nums2 = [-1,1,0,-3,3]
ans2 = [0,0,9,0,0]

print(ans == Solution().productExceptSelf(nums))
print(ans2 == Solution().productExceptSelf(nums2))