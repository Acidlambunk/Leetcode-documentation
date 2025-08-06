class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
    
'''How it works:
1. Split the input string `s` into a list of words using `split()`, which handles multiple spaces by default.
2. Reverse the list of words using the `reverse()` method.
3. Join the reversed list back into a single string with a single space between each word using `" ".join()`.
4. Return the resulting string.
'''