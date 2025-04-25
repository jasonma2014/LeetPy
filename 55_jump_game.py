"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105

"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
            
        # 记录能够到达的最远位置
        farthest = 0
        
        # 遍历数组（除了最后一个元素）
        for i in range(n - 1):
            # 如果当前位置已经无法到达，直接返回False
            if i > farthest:
                return False
                
            # 更新最远可达位置
            farthest = max(farthest, i + nums[i])
            
            # 如果已经可以到达最后一个位置，直接返回True
            if farthest >= n - 1:
                return True
                
        # 检查是否能够到达最后一个位置
        return farthest >= n - 1
    