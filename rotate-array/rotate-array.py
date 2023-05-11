class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k % size
        temp = copy.deepcopy(nums)
        for i in range(size):
            rotate = (i+k) % size
            nums[rotate] = temp[i]

    def rotate_nums(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        
        