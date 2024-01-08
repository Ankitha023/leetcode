#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]+nums[j] == target):
        #             return([i,j])
        seen = {}

        for i,curr in enumerate(nums):
            # if curr not in seen:
            #     seen[curr] = i
            if target - curr in seen:
                return ([seen[target - curr],i])
            elif curr not in seen:
                seen[curr] = i
