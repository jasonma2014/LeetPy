from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # 如果起点或终点有障碍物，直接返回0
        # if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        #     return 0
            
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0] * n for _ in range(m)]
        
        # # 初始化第一个格子
        # dp[0][0] = 1
        
        # # 初始化第一行
        # for j in range(1, n):
        #     if obstacleGrid[0][j] == 0:
        #         dp[0][j] = dp[0][j-1]
                
        # # 初始化第一列
        # for i in range(1, m):
        #     if obstacleGrid[i][0] == 0:
        #         dp[i][0] = dp[i-1][0]
        
        # # 填充dp数组
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] == 0:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1] 
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = 1
        
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
                    