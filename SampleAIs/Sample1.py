import AIArena as aio
import random

class lilBuddy(aio.AI):
    def __init__(self):
        super().__init__("lilBuddy", "Connect4")

    def makeMove(self, state):
        move = random.randint(0, 6)
        return move


if __name__ == "__main__":
    ref = aio.Ref()

    ai1 = lilBuddy()

    aio.upload(ai1, "f9PzYd7xBxUUeRyEomVm")
    #ai2 = aio.Human_Connect4()
    #ref.createGame("Connect4", [ai1, ai2])
    #ref.runGame(True)
