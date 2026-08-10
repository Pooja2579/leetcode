class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # moves = (1-1)+ (2-1)+(3-1) = 0+1+2= 3
        n = len(nums)
        move = sum(nums) - n*min(nums)
        return move