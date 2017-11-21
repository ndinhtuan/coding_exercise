'''
This problem is from: 
https://leetcode.com/problems/reverse-string/description/

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    # solution 2
    def reverseString2(self, s):
        return ''.join(reversed(s))

# test cases 
tests = {   'abc' : 'cba', 
            '' : '', 
            'a': 'a'}

for key, value in tests.iteritems():
    assert Solution().reverseString(key) == value, 'Incorrect at input ' + key 

print 'All tests passed!'
