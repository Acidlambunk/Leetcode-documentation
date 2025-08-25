class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i,num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if right_sum == left_sum:
                return i
            left_sum += num
        return -1

'''how it works:
1. We calculate the total sum of the array elements.
2. We initialize a left sum variable to 0.
3. We iterate through the array, calculating the right sum as the total sum minus the left sum and the current element.
4. If the left sum equals the right sum, we have found the pivot index and return it.
5. If no pivot index is found, we return -1.
'''