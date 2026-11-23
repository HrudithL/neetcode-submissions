class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        # concept is just a set per row and per col and per square and use them to track already seen values
        # only one complete board iteration required now, just like checking for duplicates in an array but now in a matrix

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in rows[r] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                squares.add((r//3, c//3))
                cols.add(c)
            rows.add(r)
        return True