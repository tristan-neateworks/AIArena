from aiolympics.AI import Player as Player

class Human_Connect4(Player):
    def __init__(self):
        super().__init__("Human", "Connect4")

    def makeMove(self, state):
        move = "-1"
        while not move.isdigit() or int(move) >=7:
            move = input("Enter column number (0-6) to place piece: ")
        return int(move)