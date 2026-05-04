class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = {}

        for i, n in enumerate(nums):
            j = target - n

            if j in output:
                return [output[j],i]
            output[n] = i
        