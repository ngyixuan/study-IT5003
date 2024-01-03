from collections import deque
class Solution:
    def __init__(self):
        self.grid = [
                        ".........",
                        ".........",
                        "...#.....",
                        "....#....",
                        ".........",
                        ".........",
                    ]
        self.cols = 9
        self.rows = 6
        self.growth_position = set()
        self.direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


    #iterate throught the initial bacteria position and record the posiiton in a set
    def initialize(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if(self.grid[row][col]=='#'):
                    self.growth_position.add((row,col))
 
    #update the current growth position in a new set by adding its 8 direction
    def count_number(self):
        for _ in range(0):
            new_growth_position = set()
            for initial_row, initial_col in self.growth_position:
                for dir_row, dir_col in self.direction:
                    new_growth_position.add((initial_row+dir_row, initial_col+dir_col))
            self.growth_position.update(new_growth_position)
        print((len(self.growth_position)))


solution = Solution()
solution.initialize()
solution.count_number()



    