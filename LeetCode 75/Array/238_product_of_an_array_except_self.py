class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        result = [0] * length
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1] 
        for i in range(length - 2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(length):
            result[i] = suffix[i] * prefix[i]
        return result
    
'''How it works:
1. Initialize three lists: `prefix`, `suffix`, and `result`, all of the same length as `nums`.
2. Fill the `prefix` list such that each element at index `i` contains the product of all elements before index `i` in `nums`.
3. Fill the `suffix` list such that each element at index `i` contains the product of all elements after index `i` in `nums`.
4. Compute the final result by multiplying corresponding elements from `prefix` and `suffix`.
5. Return the `result` list.
'''