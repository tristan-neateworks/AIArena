import AIArena as aio
import random
import math

def euDist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def computeBearing(a, b):
    dist=euDist(a, b)
    x=b[0]-a[0]
    y=b[1]-a[1]
    return math.degrees(math.atan2(x, y))*-1

class ArenaTest(aio.AI):
    def __init__(self, name, game):
        super().__init__(name, game)

    def makeMove(self, state):
        # Our state is as follows:
        """arPlayer["name"]=name
        arPlayer["position"]=pos
        arPlayer["health"]=health
        arPlayer["aoe"]=aoe
        arPlayer["lastmove"]=lastmove
        arPlayer["score"]=score
        arPlayer["inventory"]=inventory
        arPlayer["board"]=board"""
        
        if state is None:
            return {"action":"nop", "params":(None)}
        
        ourPos=state["position"]
        
        for i, r in enumerate(state["board"]):
            for j, c in enumerate(r):
                if c[0] is not None and i!=ourPos[0] and j!=ourPos[1]:
                    theirPos=(i, j)
                    if euDist(ourPos, theirPos)>=state["range"]:
                        bearing=computeBearing(ourPos, theirPos)
                        #print("%s target out of range. Moving closer to %f." % (self.name, bearing))
                        if bearing>=0 and bearing<90:
                            return {"action": "move", "params": (ourPos[0]-1, ourPos[1]+1)}
                        elif bearing>=90 and bearing<=180:
                            return {"action": "move", "params": (ourPos[0]-1, ourPos[1]-1)}
                        elif bearing<=0 and bearing>=-90:
                            return {"action": "move", "params": (ourPos[0]+1, ourPos[1]+1)}
                        else:# bearing<-90 and bearing>=-180:
                            return {"action": "move", "params": (ourPos[0]+1, ourPos[1]-1)}
                        
                    return {"action": "fire", "params": (i, j)}
        
        # Fire on ourselves to make the game end more quickly:
        #print("%s firing on self", self.name)
        return {"action": "fire", "params": state["position"]}


if __name__ == "__main__":
    ref = aio.Ref()

    ai1 = ArenaTest("ai1", "Arena")
    ai2 = ArenaTest("ai2", "Arena")
    ai3 = ArenaTest("ai3", "Arena")
    
    ref.createGame("Arena", [ai1, ai2, ai3])
    ref.runGame(True)

    #aio.upload(ai1, "f9PzYd7xBxUUeRyEomVm")
    #ai2 = aio.Human_Connect4()
    #ref.createGame("Connect4", [ai1, ai2])
    #ref.runGame(True)
