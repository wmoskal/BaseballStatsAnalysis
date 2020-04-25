class Player: 

    # Instance variables
    age = 0
    firstName = ""
    lastName = ""
    teamName = ""
    teamAbrv = ""
    teamLocation = ""
    player_id = 0
    positions = []
    
    def __init__(self, age=0, fn="", ln="", teamName="", teamAbrv="", location="", positions="", player_id=0): 
        self.age = age
        self.firstName = fn
        self.lastName = ln
        self.teamName = teamName
        self.teamAbrv = teamAbrv
        self.teamLocation = location
        self.positions = []
        for p in positions: 
            self.positions.add(p)
        self.player_id = player_id

    def __init__(self, **playerData):
        self.age = playerData['age']
        self.firstName = playerData['firstName']
        self.lastName = playerData['lastName']
        self.teamName = playerData['teamName']
        self.teamAbrv = playerData['teamAbrv']
        self.teamLocation = playerData['teamLocation']
        self.positions = playerData['positions']
        self.player_id = playerData['player_id']

    def __eq__(self, other):
        if self.player_id == other.player_id:
            return True

    def getPrimaryPosition(): 
        return self.positions[0]

    def setPrimaryPosition(primary):
        self.positions.insert(0, primary)

    def removePosition(pos): 
        if pos in self.positions:
            self.positions.remove(pos)
        return
