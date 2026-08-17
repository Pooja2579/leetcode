class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        current_max = 0
        res = 0

        for i in range(len(arr)):
            current_max = max(arr[i], current_max)

            if current_max == i:
                res += 1
        return res