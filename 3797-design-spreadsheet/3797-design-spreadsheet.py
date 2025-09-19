class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.grid = [[0] * self.cols for _ in range(rows)]

    def _parseCell(self, cell: str):
        """Convert cell reference like 'B2' -> (row_index, col_index)."""
        col = ord(cell[0]) - ord('A')        # 'A' -> 0, 'B' -> 1, ...
        row = int(cell[1:]) - 1              # '1' -> 0 (zero-indexed)
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parseCell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parseCell(cell)
        self.grid[row][col] = 0

    def _getOperandValue(self, operand: str) -> int:
        if operand.isdigit():                # if it's a number
            return int(operand)
        else:                                # otherwise it's a cell reference
            row, col = self._parseCell(operand)
            return self.grid[row][col]

    def getValue(self, formula: str) -> int:
        # formula is always like "=X+Y"
        formula = formula[1:]                # remove leading "="
        left, right = formula.split("+")
        return self._getOperandValue(left) + self._getOperandValue(right)
