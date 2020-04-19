from Player import Player
class Batter(Player):

    # Instance Variables
    gamesPlayed = 0
    atBats = 0
    hits = 0
    doubles = 0
    triples = 0
    homeRuns = 0
    walks = 0
    runs = 0
    rbis = 0
    battingAverage = 0.0
    strikeouts = 0
    stolenBases = 0 
    slg = 0.0
    onBasePercentage = 0.0
    ops = 0.0


    # Secondary Constructor
    def __init__(self, age, fn, ln, teamName, teamAbrv, location, positions, player_id):
        super().__init__(age, fn, ln, teamName, teamAbrv, location, positions, player_id)
    
    # passes player data and batter data as kwargs
    def __init__(self, age, fn, ln, teamName, teamAbrv, location, positions, player_id, **batterData):
        self.__init__(age, fn, ln, teamName. teamAbrv, location, positions, player_id)
        self.gamesPlayed = batterData['gamesPlayed']
        self.atBats = batterData['atBats']
        self.hits = batterData['hits']
        self.doubles = batterData['doubles']
        self.triples = batterData['triples']
        self.homeRuns = batterData['homeRuns']
        self.runs = batterData['runs']
        self.rbis = batterData['rbis']
        self.walks = batterData['walks']
        self.battingAverage = batterData['battingAverage']
        self.strikeouts = batterData['strikeouts']
        self.stolenBases = batterData['stolenBases']
        self.slg = batterData['slg']
        self.onBasePercentage = batterData['onBasePercentage']
        self.ops = batterData['ops']

    def __init__(self, **batterData):
        self.age = batterData['age']
        self.firstName = batterData['firstName']
        self.lastName = batterData['lastName']
        self.teamName = batterData['teamName']
        self.teamAbrv = batterData['teamAbrv']
        self.location = batterData['location']
        self.positions = batterData['positions']
        self.player_id = batterData['player_id']
        self.gamesPlayed = batterData['gamesPlayed']
        self.atBats = batterData['atBats']
        self.hits = batterData['hits']
        self.doubles = batterData['doubles']
        self.triples = batterData['triples']
        self.homeRuns = batterData['homeRuns']
        self.runs = batterData['runs']
        self.rbis = batterData['rbis']
        self.walks = batterData['walks']
        self.battingAverage = batterData['battingAverage']
        self.strikeouts = batterData['strikeouts']
        self.stolenBases = batterData['stolenBases']
        self.slg = batterData['slg']
        self.onBasePercentage = batterData['onBasePercentage']
        self.ops = batterData['ops']

    # get the number of singles a player has gotten from his other stats
    def getSingles():
        if hits <= 0:
            return 0
        else:
            return this.hits - this.doubles - this.triples - this.homeRuns