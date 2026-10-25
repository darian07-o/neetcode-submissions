class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])
        startRow = 0
        startCol = 0
        boxes = rows * cols
        while (len(result) < boxes):
            #top
            for i in range(startCol, cols):
                result.append(matrix[startRow][i])
            startRow += 1

            #right
            for i in range(startRow, rows):
                result.append(matrix[i][cols - 1])
            cols -= 1

            if startRow < rows:
                for i in range(cols - 1, startCol - 1, -1):
                    result.append(matrix[rows - 1][i])
                rows -= 1

            #left
            if startCol < cols:
                for i in range(rows - 1, startRow - 1, -1):
                    result.append(matrix[i][startCol])
                startCol += 1
        return result


        