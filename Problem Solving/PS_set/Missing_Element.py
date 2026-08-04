from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []

        for i in range(len(nums) - 1):
            for j in range(nums[i] + 1, nums[i + 1]):
                answer.append(j)

        return answer
