import AIArena.games as games


class Ref:
    """ This class coordinates, executes, and determines which AI or player won a given (locally run) game. It is reasonable to assume that AIOlympics uses a similar process to perform game execution for the purposes of AI development.
    """
    
    #def __init__(self, state=None):
    def createGame(self,game,players):
        """ Initializes a given game with a given set of players (human and/or AI). This takes the place of a constructor.
        
        :param game: Name of a game to set up (currently, only "Connect4" is implemented)
        :type game: string
        :param players: List of :class:`aiarena.AI.Player` objects to have play the game.
        :type players: list
        """
        self.pids = [x.name for x in players]
        self.players = players
        self.moves = []
        self.gameName=game
        
        print("Creating game: %s" % game)
        if game == "Connect4":
            self.game = games.Connect4(None, self.pids)
        elif game=="Arena":
            self.game=games.Arena(None, self.pids)


    def runGame(self, display=False):
        """ Steps through player moves (in order) until the game specified by createGame() is finished.
        
        :param display: Whether or not to print every move and game state as they occur. Default value is False
        :type display: bool
        :return: The final game state. 
        :rtype: dict
        """
        
        # Arena unfortunately needs special treatment in terms of how it's run:
        if self.gameName=="Arena":
            print("Running Arena")
            #print(self.game.state)
            while "Winner" not in self.game.state:
                #print("Turn: %d" % self.game.state["turn"])
                for p in self.players:
                    # playerArr has the player-accessible player state:
                    if p.name in self.game.playerArr:
                        move=p.makeMove(self.game.playerArr[p.name])
                        self.moves.append(move)
                        if not self.move(move, p.name):
                            #print("player %s made invalid move" % p.name)
                            #print("Move: ", move)
                            pass
                            #return -1
                    elif display:
                        #print("Skipping player "+p.name)
                        pass
                if display:
                    self.game.print()
        else:
            while "Winner" not in self.game.state:
                #print("turn", self.game.state["turn"])
                move = self.players[self.game.state["turn"]].makeMove(self.game.state)
                self.moves.append(move)
                if not self.move(move):
                    return -1
                if display:
                    self.game.print()
        return self.game.state["Winner"]


    def move(self, move, name=None):
        """ Runs the move passed.
        
        :param move: The move to directly run in-game.
        :return: Whether or not the move was successful.
        :rtype: bool
        """
        if name is None:
            if self.game.validateMove(move):
                self.game.makeMove(move)
                self.game.postMove()
                return True
        else:
            if self.game.validateMove(move, name):
                self.game.makeMove(move, name)
                self.game.postMove()
                return True
        return False

    def endGame(self):
        pass

if __name__ == "__main__":
    ai1 = lilBuddy()
    ai2 = lilBuddy()
    R = Ref()

    R.createGame("Connect4", [ai1, ai2])
    winner = R.runGame()
    print(winner, R.players[winner].name)
