class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < k:
            return 0

        current_sum = sum(nums[:k])  # Calculate sum of the first window
        max_sum = current_sum

        for i in range(k, n):
            current_sum += nums[i] - nums[i - k]  # Slide the window
            max_sum = max(max_sum, current_sum)

        return max_sum/k
    
'''how it works:
1. Initialize the sum of the first k elements.
2. Slide the window across the array, updating the sum by adding the next element and removing the first element of the previous window.
3. Keep track of the maximum sum encountered.
4. Return the maximum sum divided by k to get the average.
'''