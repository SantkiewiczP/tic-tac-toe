class Matrix:

    def __init__(self):
        self.grid = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]

    def render(self):
        for row in self.grid:
            for slot in row:
                print(slot, end="  ")
            print()
        return self.grid

    def place(self, location, symbol):
        if self.grid[location[0]][location[1]] != "_":
            return False
        self.grid[location[0]][location[1]] = symbol
        return True

    def has_winner(self):
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != "_":
            return True
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != "_":
            return True
        elif self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != "_":
            return True
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != "_":
            return True
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != "_":
            return True
        elif self.grid[0][0] == self.grid[0][1] == self.grid[0][2] != "_":
            return True
        elif self.grid[1][0] == self.grid[1][1] == self.grid[1][2] != "_":
            return True
        elif self.grid[2][0] == self.grid[2][1] == self.grid[2][2] != "_":
            return True
        else:
            return False

    def clear(self):
        self.__init__()
