class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [''] * numRows
        row_index = 0
        direction = 1  # 1 for down, -1 for up

        for char in s:
            rows[row_index] += char

            row_index += direction

            if row_index == numRows:
                row_index = numRows - 2
                direction = -1
            elif row_index == -1:
                row_index = 1
                direction = 1

        return ''.join(rows)