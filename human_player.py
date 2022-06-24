from player import Player


class HumanPlayer(Player):
    def make_decision(self, grid):
        return [int(x) for x in input(f"Where would you like to place {self.symbol}? (Syntax is X,Y): ").split(",")]