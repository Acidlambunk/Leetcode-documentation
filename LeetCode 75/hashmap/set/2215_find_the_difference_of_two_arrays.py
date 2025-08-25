
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        snums1 = set(nums1)
        snums2 = set(nums2)
        answer = []
        res = []

        for num in snums1:
            if num not in snums2:
                res.append(num)
        answer.append(res)
        res=[]
        for num in snums2:
            if num not in snums1:
                res.append(num)
        answer.append(res)
        return answer


'''how to do it:
create set from the list to ensure no dupplicate
use the loop to loop through the first set and check and add the first set into an empty res array then append the res array to the empty answer list
then re initate the empty array and use the same method to check in set 1 and append then retyrn the answer'''