class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = sum(nums[0::2])
        return answer