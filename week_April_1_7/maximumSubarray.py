"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp.values())
