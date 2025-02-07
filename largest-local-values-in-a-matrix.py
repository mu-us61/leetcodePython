# https://leetcode.com/problems/largest-local-values-in-a-matrix/
# 2373. Largest Local Values in a Matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxlocal=[]
        n=len(grid)
        submatrices=[]
        for i in range(n-2):
            for j in range(n-2):
                submatrix =[]
                for k in range(3):
                    row=[]
                    for l in range(3):
                        row.append(grid[i+k][j+l])
                    submatrix.append(row)
                submatrices.append(submatrix)

        # print(submatrices)

        maxLocal = [max(map(max, submatrix)) for submatrix in submatrices]
        result = [maxLocal[i:i + (n - 2)] for i in range(0, len(maxLocal), (n - 2))]
        
        return result

"""
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
n=len(grid)
print (f"n={n}")
for i in range(n-2):
    for j in range(n-2):
        print(f"3×3 Submatrix starting at ({i}, {j}):")
        for k in range(3):
            for l in range(3):
                print(grid[i+k][j+l], end=" ")
            print()
        print("----")

"""



"""
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
n=len(grid)
submatrices=[]
for i in range(n-2):
    for j in range(n-2):
        submatrix =[]
        for k in range(3):
            row=[]
            for l in range(3):
                row.append(grid[i+k][j+l])
            submatrix.append(row)
        submatrices.append(submatrix)

print(submatrices)
"""



"""
submatrix=[[[9, 9, 8], [5, 6, 2], [8, 2, 6]], [[9, 8, 1], [6, 2, 6], [2, 6, 4]], [[5, 6, 2], [8, 2, 6], [6, 2, 2]], [[6, 2, 6], [2, 6, 4], [2, 2, 2]]]

maxLocal = [max(map(max, submatrix)) for submatrix in submatrices]

print(maxLocal)
"""

