class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)

        result = []

        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxcandies)
        return result
'''
How it works:
1. Find the maximum number of candies any kid has using `max(candies)`.
2. Initialize an empty list `result` to store boolean values.
3. Iterate through each kid's candy count:
   - Check if adding `extraCandies` to the current kid's candies makes it greater than or equal to `maxcandies`.
   - Append the result of this check (True or False) to the `result` list.
4. Return the `result` list containing boolean values indicating whether each kid can have the greatest number of candies.
'''
