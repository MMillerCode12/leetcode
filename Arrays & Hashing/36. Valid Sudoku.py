class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            
            valid_col = []
            
            for x in range(len(board)):
                if board[x][i] in valid_col:
                    return False
                
                if board[x][i] != ".":
                    valid_col.append(board[x][i])

        
        for i in range(len(board)):

            valid_row = []

            print(board[i])
            
            for x in range(len(board)):

                if board[i][x] in valid_row:
                    return False
                
                if board[i][x] != ".":
                    valid_row.append(board[i][x])


        for i in range(0, len(board), 3):
            for x in range(0, len(board), 3):

                valid_box = []

                for j in range(i, i+3):
                    for y in range(x, x+3):

                        if board[j][y] in valid_box:
                            return False
                        
                        if board[j][y] != ".":
                            valid_box.append(board[j][y])


        return True
        
