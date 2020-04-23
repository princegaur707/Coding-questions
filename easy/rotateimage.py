class Solution:
    def rotate(self, matrix):
        matrix[::] = zip(*matrix[::-1])#for clockwise rotation
        matrix1[::] = reversed(zip(*matrix))
        print("After anti-clockwise:  ",matrix1)
        return matrix
obj=Solution()
print("After clockwise rotation: ",obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))
                
                
                
                