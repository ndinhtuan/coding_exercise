'''
This problem is from
https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?



'''

# idea: 
# 1. hash table (counting) O(n+n)
# 2. sorting O(nlogn)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False 
        d = {}
        for c in s: 
            if c in d: 
                d[c] += 1
            else:
                d[c] = 1
        for c in t: 
            if c not in d: 
                return False 
            d[c] -= 1
            if d[c] < 0: return False 
        return True 

tests = [ (['', ''], True),
          (['t', 't'], True),
          (['t', 'v'], False),
          (['t', 'tv'], False),
          (['tv', 'vt'], True),
          (['vuhuutiep', 'vutiephuu'], True)]

for test in tests:
    assert Solution().isAnagram(test[0][0], test[0][1]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"