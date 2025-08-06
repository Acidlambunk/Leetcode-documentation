class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j+=1
            
        return i == len(s)
            
'''How it works:
1. Initialize two pointers `i` and `j` to 0, representing the current index in `s` and `t`, respectively.
2. Use a while loop to iterate through both strings until either pointer reaches the end of its respective string.
3. If the characters at the current indices match (`s[i] == t[j]`), increment the pointer `i` to check the next character in `s`.
4. Always increment the pointer `j` to continue checking characters in `t`.
5. After the loop, check if `i` has reached the length of `s`. If it has, it means all characters in `s` were found in `t` in order, so return `True`. Otherwise, return `False`.
'''