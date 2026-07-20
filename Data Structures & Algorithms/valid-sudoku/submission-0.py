class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seen = set()
            for i in range(9):
                val = board[r][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # check cols
        for c in range(9):
            seen = set()
            for i in range(9):
                val = board[i][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # check sub-boxes
        for s in range(9):
            seen = set()
            sr = (s // 3) * 3
            sc = (s % 3) * 3
            for i in range(9):
                r = i // 3 + sr 
                c = i % 3 + sc
                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        return True