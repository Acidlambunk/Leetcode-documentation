class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        
        zero = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len - 1 
        
''' how it works:
1. Initialize two pointers, `left` and `right`, to represent the current window.
2. Use a counter to track the number of zeros in the current window.
3. Expand the `right` pointer to include more elements until the count of zeros exceeds 1.
4. If it exceeds, move the `left` pointer to reduce the window size until the count of zeros is within 1.
5. Update the maximum length of the window whenever a valid window is found.
6. Return the maximum length found minus one, as we need to remove one element (the zero).
'''