from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    seen = set()
    for x, row in enumerate(board):
        for y, item in enumerate(row):
            #print(f'x: {x}, y:{y}, {row}, {item}')
            if item != ".":
                if ("row", x, item) in seen:
                    print(("row", x, item))
                    return False
                if ("col", y, item) in seen:
                    print("col", y, item)
                    return False
                if ("box", x//3, y//3, item) in seen:
                    print("box", x//3 , y//3, item)
                    return False

                seen.add(("row", x, item))
                seen.add(("col", y, item))
                seen.add(("box", (x//3), (y//3), item))
    return True


validBoard = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

invalidBoard = [
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(validBoard))
print(isValidSudoku(invalidBoard))