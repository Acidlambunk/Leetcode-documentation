class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j+=1
            
        return i == len(s)
            
'''How it works:
1. Initialize two pointers repr(i) and repr(j) to 0, representing the current index in repr(s) and repr(t), respectively.
2. Use a while loop to iterate through both strings until either pointer reaches the end of its respective string.
3. If the characters at the current indices match (repr(s[i]) == repr(t[j])), increment the pointer repr(i) to check the next character in repr(s).
4. Always increment the pointer repr(j) to continue checking characters in repr(t).
5. After the loop, check if repr(i) has reached the length of repr(s). If it has, it means all characters in repr(s) were found in repr(t) in order, so return True. Otherwise, return False.
'''