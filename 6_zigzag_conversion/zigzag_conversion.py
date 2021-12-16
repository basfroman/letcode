class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) < 3:
            return s

        result_string = ''
        length = len(s)

        for row in range(numRows):

            current_index = row
            result_string += s[current_index]

            while ((numRows - row) * 2) - row <= length:

                if 0 < row < numRows - 1:
                    result_string += s[current_index + numRows + (numRows - 2) - row * 2]

                current_index = current_index + numRows + (numRows - 2)

                if current_index < length:
                    result_string += s[current_index]
        print(result_string)
        return result_string


if __name__ == '__main__':
    sol = Solution()
    # assert sol.convert('PAYPALISHIRING', numRows=4) == 'PINALSIGYAHRPI'
    # assert sol.convert('PAYPALISHIRING', numRows=3) == 'PAHNAPLSIIGYIR'
    # assert sol.convert('A', numRows=1) == 'A'
    # assert sol.convert('AB', numRows=1) == 'AB'
    assert sol.convert('ABCDE', numRows=4) == 'ABCED'
