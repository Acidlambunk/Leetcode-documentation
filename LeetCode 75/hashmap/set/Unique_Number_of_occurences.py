from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_map = defaultdict(int)

        for s in arr:
            arr_map[s] += 1

        counts = list(arr_map.values())
        print(arr_map)

'''how it works:
first set the default initiate the dict in arr_map
second they see for every key in arr bump up 1 if it sees again so 1 one time is 1:1 one two time is 1:2 etc
last is use arr_map.values to print the values
then return the length of counts if its the same as set of length of count it means there is no duplicate in the answer theat means the 
number of occurance is unique '''