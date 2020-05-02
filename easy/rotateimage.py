class Solution:
    def rotate(self, matrix):
        matrix[::] = zip(*matrix[::-1])#for clockwise rotation
        #matrix2 = reversed(matrix)
        #print("After anti-clockwise:  ",list(matrix2))
        return matrix
obj=Solution()
print("After clockwise rotation: ",obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix[0])
#         for i in range(n // 2 + n % 2):
#             for j in range(n // 2):
#                 tmp = [0] * 4
#                 row, col = i, j
#                 # store 4 elements in tmp
#                 for k in range(4):
#                     tmp[k] = matrix[row][col]
#                     row, col = col, n - 1 - row
#                 # rotate 4 elements   
#                 for k in range(4):
#                     matrix[row][col] = tmp[(k - 1) % 4]
#                     row, col = col, n - 1 - row


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m) 
        def transpose():
            
            for col in range(n):
                
                for row in range(col):

                    m[row][col],m[col][row] = m[col][row],m[row][col]
        
        transpose()

        for row in m:
            row.reverse()
        
        return m