'''
This problem is from
https://leetcode.com/problems/single-number/description/

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''

# idea: using xor operator, linear, no extra memory

class Solution(object):
    def singleNumber(self, a):
        res = 0 
        for num in a: 
            res ^= num 
        return res 

tests = [ ([1], 1),
         ([1, 2, 1], 2), 
         ([1, 2, 3, 3, 2, 1, 4, 4, 5], 5)]

for test in tests:
    assert Solution().singleNumber(test[0]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"