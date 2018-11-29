# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution(object):

    def helper(self, s, k, memory):
        if k == 0:
            return 1
        start = len(s) - k
        if s[start] == '0':
            return 0
        if memory[k] != 0:
            return memory[k]
        result = self.helper(s, k - 1, memory)
        if k >= 2 and int(s[start:start + 2]) <= 26:
            result += self.helper(s, k - 2, memory)
        memory[k] = result
        return result

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memory = [0] * (len(s) + 1)
        return self.helper(s, len(s), memory)

solu = new Solution()
print(solu('226'))