from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        # Find range to handle negatives
        min_val = min(nums)
        max_val = max(nums)
        
        # Radix sort in base 10, but handle sign separately
        # We'll do LSD radix sort on absolute values with sign handling
        
        # Separate based on sign
        negatives = []
        positives = []
        
        for num in nums:
            if num < 0:
                negatives.append(-num)  # Store positive version
            else:
                positives.append(num)
        
        # Sort positives (regular radix sort)
        if positives:
            positives = self.radix_sort(positives)
        
        # Sort negatives (radix sort on absolute values, then reverse)
        if negatives:
            negatives = self.radix_sort(negatives)
            negatives = [-x for x in reversed(negatives)]
        
        return negatives + positives
    
    def radix_sort(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        max_val = max(nums)
        exp = 1
        
        while max_val // exp > 0:
            output = [0] * len(nums)
            count = [0] * 10
            
            for num in nums:
                digit = (num // exp) % 10
                count[digit] += 1
            
            for i in range(1, 10):
                count[i] += count[i-1]
            
            for num in reversed(nums):
                digit = (num // exp) % 10
                output[count[digit] - 1] = num
                count[digit] -= 1
            
            nums = output
            exp *= 10
        
        return nums
        # if not nums:
        #     return nums
        # max_val = max(nums)
        # exp = 1

        # while max_val//exp> 0:
        #     output = [0]* len(nums)
        #     count = [0]* 10

        #     for num in nums:
        #         digit = (num //exp) % 10
        #         count[digit] +=1

        #     for i in range(1, 10):
        #         count[i] += count[i-1]

        #     for num in reversed(nums):
        #         digit = (num//exp)%10
        #         output[count[digit]-1] = num
        #         count[digit] -=1


        #     nums = output
        #     exp *=10

        # return nums
        