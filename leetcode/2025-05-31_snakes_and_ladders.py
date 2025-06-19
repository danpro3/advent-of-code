# %%
from heapq import heapify, heappush, heappop

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.n = len(board)
        # test code to get the board value
        # for num in range(1,self.n**2+1):
        #     print('num = ',num)
        #     v = self.get_value(board,num)
        #     print(num, v)

        curr = 1 # starting square
        self.todo = []
        self.visited = set()
        heappush(self.todo,(0, curr))

        while(self.todo):
            # print(self.todo)
            score, self.todo = self.roll(board)
            # print(f'score = {score}, length todo = {len(self.todo)}')
        return score

    def roll(self,board):
        score, curr = heappop(self.todo)
        # print('popped score = ', score, 'curr = ', curr)
        if curr in self.visited:
            return score, self.todo
        else:
            self.visited.add((curr))

        # now add the outcomes of die rolls
        for die in range(1,7):
            # print('die = ',die, 'curr = ',curr)
            if curr + die > self.n**2:
                return
            elif curr + die == self.n**2:
                print('Die roll to end. score = ',score+1)
                self.todo = []
                return score+1, self.todo
            else:
                next = curr + die
                if self.get_value(board,next) != -1:
                    next = self.get_value(board,next)
                    # print('next = ',next)
                    if next == self.n**2:
                        print('Ladder to end. score = ',score)
                        self.todo = []
                        return score+1, self.todo
                    else:
                        heappush(self.todo, (score+1, next))
                        # print(self.todo)
        return score, self.todo

    def get_value(self,board,num):
        row = self.n-1 - (num-1) // self.n
        if row % 2 == 0:  # reverse the row
            col = self.n-1 - (num-1) % self.n
        else:
            col = (num-1) % self.n
        value = board[row][col]
        # print('num', num, 'row', row, 'col', col, 'value', value)
        return value

# main
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]] # 4
# board = [[-1,-1],[-1,3]] # 1

# board = [[-1,-1,-1],[-1,9,8],[-1,8,9]] # 1
_=[print(x) for x in board]
solution = Solution()
solution.snakesAndLadders(board)


# %%
