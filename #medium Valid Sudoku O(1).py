def isValidSudoku(self, board: List[List[str]]) -> bool:
    col, box = [set() for _ in range(9)], [set() for _ in range(9)]
        
    for i in range(9):
        row = set()

        for j in range(9):
            if board[i][j] != '.':
                num, idx = int(board[i][j]), i // 3 * 3 + j // 3

                if num in row or num in col[j] or num in box[idx]:
                    return False

                row.add(num)
                col[j].add(num)
                box[idx].add(num)

    return True
