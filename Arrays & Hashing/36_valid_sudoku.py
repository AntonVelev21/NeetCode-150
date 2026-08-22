class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = {i: {} for i in range(len(board))}
        cols = {i: {} for i in range(len(board))}
        boxes = {i: {} for i in range(len(board))}
        digits = {str(i) for i in range(1, 10)}
        counter = 0

        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                counter += 3
            for j, col in enumerate(row):
                if j % 3 == 0 and j != 0:
                    counter += 1
                if col in rows[i] or col in cols[j] or col in boxes[counter]:
                    return False
                if col in digits:
                    rows[i][col] = 'Yes'
                    cols[j][col] = 'Yes'
                    boxes[counter][col] = 'Yes'
                else:
                    if col != '.':
                        return False
            counter -= 2
        return True
