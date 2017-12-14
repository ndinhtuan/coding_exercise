'''
This problem is from
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

# idea: 
# use a stack, push all open brackets into this 
# if encounter a close bracket ('), }, ]') then check if top of 
# that stack is the corresponding open bracket.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {')': '(', ']': '[', '}':'{'}
        stack = []
        for c in s: 
            if c in pair:
                if not stack or pair[c] != stack.pop(): return False 
            else:
                stack.append(c)
        return not stack # empty at the end 

tests = [ ('()', True),
          ('', True),
          ('({)}', False),
          (')(', False),
          ('({}([])[()])', True)]

for test in tests:
    assert Solution().isValid(test[0]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"