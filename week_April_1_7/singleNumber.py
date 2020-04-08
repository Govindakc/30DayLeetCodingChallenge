"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
Note: Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""
class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """    
    def singleNumber(self, nums):
        n = 0
        for num in nums:
            # Using XOR
            n = n ^ num
        return n
