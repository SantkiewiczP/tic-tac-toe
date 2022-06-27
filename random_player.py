import random

from player import Player


class RandomPlayer(Player):
    def make_decision(self, grid):
        column = random.randint(0, len(grid) - 1)
        row = random.randint(0, len(grid[0]) - 1)
        return [column, row]
