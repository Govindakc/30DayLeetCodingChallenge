"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum 
of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which 
does not include 1. Those numbers for which this process ends in 1 are 
happy numbers.

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        def helper(n):
            nString = str(n)
            nList = [int(i) for i in nString]
            return nList
        
        while n > 1 and n not in seen:
            seen.add(n)
            nList = helper(n)
            n = sum(map(lambda x:x**2, nList))

        return not n in seen


