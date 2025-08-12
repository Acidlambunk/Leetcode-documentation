class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

''' how it works:
1. Initialize two pointers, repr(left) and repr(right), to represent the current window.
2. Use a counter to track the number of zeros in the current window.
3. Expand the repr(right) pointer to include more elements until the count of zeros exceeds repr(k).
4. If it exceeds, move the repr(left) pointer to reduce the window size until the count of zeros is within repr(k).
5. Update the maximum length of the window whenever a valid window is found.
6. Return the maximum length found.
'''