"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos1, pos2 = 0, len(matrix) - 1
        while pos1 < pos2:
            add = 0
            while add < pos2 - pos1:
                # 左上角为0， 右上角为1， 右下角为2， 左下角为3
                temp = matrix[pos2-add][pos1]
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add] # 3 = 2
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2] # 2 = 1
                matrix[pos1+add][pos2] = matrix[pos1][pos1+add] # 1 = 0
                matrix[pos1][pos1+add] = temp # 0 = temp
                add = add + 1
            pos1 = pos1 + 1
            pos2 = pos2 - 1

# Compare this snippet from 48_rotate_image.py:
# """
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in