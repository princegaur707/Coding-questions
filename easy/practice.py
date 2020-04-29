class Solution:
    def rotate(self, matrix):
        matrix1 = zip(*matrix[::-1])#for clockwise rotation
        matrix2 = reversed(matrix)
        print("After anti-clockwise:  ",list(matrix2))
        return list(matrix1)
obj=Solution()
print("After clockwise rotation: ",obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))