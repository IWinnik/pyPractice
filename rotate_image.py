from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix) - 1
    rotated = []
    for i in range(n + 1):
        rotated.append([None] * (n + 1))
    for row, el in enumerate(matrix):
        for col, item in enumerate(el):
            rotated[col][n - row] = item

    matrix[:] = rotated


matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate(matrix)
print(matrix)