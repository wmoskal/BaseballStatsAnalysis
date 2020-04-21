class Team:
    lineup = {}
    rotation = {}
    bullpen = {}
    bench {}
    teamName = ""
    teamAbrv = ""
    location = ""

    def __init__(self, lineup={}, rotation={}, bullpen={}, bench={}, teamName="", teamAbrv="", location=""):
        self.lineup = lineup
        self.rotation = rotation
        self.bullpen = bullpen
        self.bench = bench
        self.teamName = teamName
        self.teamAbrv = teamAbrv
        self.location = location

    def addToLineup(self, position, player):
        self.lineup[position] = player
    
    def addToRotation(self, position, player):
        self.rotation[position] = player

    def addToBullpen(self, position, player):
        self.rotation[position] = player
    
    def addToBench(position, player):
        self.bench[position] = player

    def removeFromLineup(self, position):
        del self.lineup[position]

    def removeFromRotation(self, position):
        del self.rotation[position]

    def removeFromBullpen(position):
        del self.bullpen[position]

    def removeFromBench(position):
        del self.bench[position]

    def verifyLineup(self):
        positions = self.lineup.keys()
        if 'c' in positions and '1b' in positions and '2b' in positions and '3b' in positions
            and 'ss' in positions and 'LF' in positions and 'CF' in positions and 'RF' in positions:
                return true
        return false

    def getMissingLineupPositions(self): 
        if verifyLineup():
            return None
        else:
            missingPositions = []
            requiredPositions = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']
            currentPositions = self.lineup.keys()
            return list(set(requiredPositions) - set(currentPositions))

    def verifyRotation(self):
        positions = self.rotation.keys()
        if len(positions) >= 4:
            return true
        return False

    def getMissingRotationPositions(self):
        if verifyRotation():
            return None
        else:
            return 4 - len(self.rotation.keys())
