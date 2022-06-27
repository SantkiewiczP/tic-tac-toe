from player import Player


class HumanPlayer(Player):
    def make_decision(self, grid):
        while True:
            try:
                return [int(x) for x in input(f"Where would you like to place {self.symbol}?"
                                              f" (Syntax is X,Y): ").split(",")]
            except ValueError:
                print("Oops! Only numbers allowed. Try again.")
