class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(1,len(nums)+1):
            next_sum = 0
            for k in range(i):
                next_sum += nums[k]
            lst.append(next_sum)
        return lst
