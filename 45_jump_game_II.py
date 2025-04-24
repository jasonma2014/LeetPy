"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        jumps = 0  # 跳跃次数
        current_end = 0  # 当前可达范围的边界
        farthest = 0  # 在当前可达范围内，能够到达的最远位置
        
        # 遍历数组（除了最后一个元素）
        for i in range(n - 1):
            # 更新最远可达位置
            farthest = max(farthest, i + nums[i])
            
            # 如果已经可以到达最后一个位置，直接返回当前跳跃次数+1
            if farthest >= n - 1:
                return jumps + 1
                
            # 当到达当前可达范围的边界时，增加跳跃次数
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
                