class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''.join([str(item) for item in digits])
        return list(map(int, list(str(int(result)+1))))

