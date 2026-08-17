class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        current_max = -1
        res= 0
        

        for i, n in enumerate(arr):
            current_max = max(n, current_max)

            if current_max == i:
                res +=1

        return res