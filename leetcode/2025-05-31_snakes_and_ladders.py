# %%
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
      # Start here
        self.n = len(board)
        self.n2 = len(board)**2
        # test code to get the board value
        # for num in range(1,self.n**2+1):
            # v = self.get_value(board,num)
            # print('square = ',num, 'value = ',v)

        curr = 1 # starting square
        self.score = 0
        self.todo = [(0, curr)]
        self.visited = set()

        while(self.todo):
            # print(self.todo)
            # score, solved, self.todo = self.roll(board)
            # score, solved = self.roll(board)
            solved = self.roll(board)
            # print(f'score = {score}, length todo = {len(self.todo)}')
            if solved:
                return self.score
        return -1
        
    def get_value(self,board,num):
        row = self.n-1 - (num-1) // self.n
        if (self.n - row) % 2 == 0:  # reverse the row
            col = self.n-1 - (num-1) % self.n
        else:
            col = (num-1) % self.n
        # value = board[row][col]
        # print('num', num, 'row', row, 'col', col, 'value', value)
        return board[row][col]

    def roll(self,board):
        score, curr = self.todo.pop(0)
        # print('todo: ',self.todo)
        # print('visited: ',self.visited)
        # print('popped: score = ', score, 'curr = ', curr)
        if curr in self.visited:
            return False
        else:
            self.visited.add(curr)

        # now add the outcomes of die rolls
        for die in range(1,7):
            next = curr + die
            self.score = score + 1
            # print('die = ',die, 'curr = ',curr)
            if next < self.n2:
                next_value = self.get_value(board,next)
                if next_value == -1:
                    self.todo.append((self.score, next))
                else:
                    # print('next = ',next)
                    if next_value == self.n2:
                        # print('Ladder to end. score = ',score)
                        return True
                    else:
                        # print('pushing next_value: ',next_value)
                        self.todo.append((self.score, next_value))
                        # print(self.todo)
            else:
                # print('Die roll ', die,'to end. score = ',score+1)
                return True
        return False

# main
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]] # 4
board = [[-1,-1],[-1,3]] # 1
board = [[-1,-1,-1],[-1,9,8],[-1,8,9]] # 1
board = [[1,1,-1],[1,1,1],[-1,1,1]] # -1
board = [[2,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]] # 4

_=[print(x) for x in board]
solution = Solution()
solution.snakesAndLadders(board)

# %%
