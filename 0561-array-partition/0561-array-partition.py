class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = sum(sorted(nums)[::2])
        return answer