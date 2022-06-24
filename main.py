import random
from art import logo
from matrix import Matrix
from human_player import HumanPlayer
from random_player import RandomPlayer

m = Matrix()
p = HumanPlayer("X")
a = RandomPlayer("O")

print(logo)


current_player = p
round_count = 0
while True:
    m.clear()
    choice = input("Would you like to play? Type 'y' or 'n': ").lower()
    if choice == 'y':
        while round_count < 9:
            round_count += 1
            m.render()
            print("---------")
            while not m.place(current_player.make_decision(m.grid), current_player.symbol):
                if isinstance(current_player, HumanPlayer):
                    print("This is not a valid location to place your symbol")
                pass

            if m.has_winner():
                break

            if current_player == p:
                current_player = a
            else:
                current_player = p
        m.render()

        if m.has_winner():
            print(f"Player {current_player.symbol} won!")
        else:
            print("It's a draw!")
            break
    else:
        print("Goodbye")
        break
