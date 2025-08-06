import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1 :
            return ""

        max_len = math.gcd(len(str1), len(str2))
        return str1[:max_len]
    
'''How it works:
1. Check if concatenating `str1` and `str2` in both orders results in the same string. If not, return an empty string.
2. Calculate the greatest common divisor (GCD) of the lengths of `str1` and `str2` using `math.gcd`.
3. Return the substring of `str1` from the start to the length of the GCD, which is the longest common prefix that can form both strings.
'''
        