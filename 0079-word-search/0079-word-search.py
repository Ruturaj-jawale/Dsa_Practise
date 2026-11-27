class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows , cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return  False
        board_cnt = Counter(ch for row in board for ch in row)

        if any(board_cnt[ch] < cnt for ch, cnt in Counter(word).items() ):
            return False

        def dfs(x:int, y:int,idn:int) -> bool:
            if idn == len(word):
                return True

            if (x < 0 or x >= rows  or y <0 or y  >= cols or board[x][y] != word[idn] ):
                    return False
                
            temp = board[x][y]
            board[x][y] = '#'

            found =(
                dfs(x+1,y,idn+1)
                or dfs(x-1,y,idn+1)
                or dfs(x,y+1,idn+1)
                or dfs(x,y-1,idn+1)
                    )

            board[x][y] = temp
            return found
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True

        return False