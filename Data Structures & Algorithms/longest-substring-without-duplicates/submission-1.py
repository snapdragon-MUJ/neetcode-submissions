class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      n=len(s)
      for i in range(0,n):
        for j in range(i+1,n):
          for k in range(i+2,n):
            if s[i]==s[j]==s[k]:
              return j             