class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1
        