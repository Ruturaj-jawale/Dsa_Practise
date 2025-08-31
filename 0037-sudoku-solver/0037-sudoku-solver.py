class Solution:
    def solveSudoku(self, board):
        # Tracking sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize the sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)
                else:
                    empty_cells.append((i, j))

        def backtrack(k=0):
            if k == len(empty_cells):  # all filled
                return True

            i, j = empty_cells[k]
            b = (i // 3) * 3 + j // 3
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                    # Place number
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[b].add(num)

                    if backtrack(k + 1):
                        return True

                    # Undo choice
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[b].remove(num)
            return False

        backtrack()
