import Player from Player

class Pitcher(Player):

    gamesStarted = 0
    inningsPitched = 0  # Uses .1 and .2 if a pitcher got 1 or 2 outs but did not complete the inning
    earnedRuns = 0
    strikeouts = 0
    ERA = 0.0
    WHIP = 0.0
    wins = 0
    holds = 0
    saves = 0
    basesAllowed = 0

    def __init__(self, age, fn, ln, teamName, teamAbrv, location, positions, player_id):
        super().__init__(age, fn, ln, teamName, teamAbrv, location, positions, player_id)

    def __init__(self, **pitcherData):
        self.age = batterData['age']
        self.firstName = pitcherData['firstName']
        self.lastName = pitcherData['lastName']
        self.teamName = pitcherData['teamName']
        self.teamAbrv = pitcherData['teamAbrv']
        self.location = pitcherData['location']
        self.positions = pitcherData['positions']
        self.player_id = pitcherData['player_id']
        self.gamesStarted = pitcherData['gamesStarted']
        self.inningsPitched = pitcherData['inningsPitched']
        self.earnedRuns = pitcherData['earnedRuns']
        self.strikeouts = pitcherData['strikeouts']
        self.ERA = pitcherData['ERA']
        self.WHIP = pitcherData['WHIP']
        self.holds = pitcherData['holds']
        self.saves = pitcherData['saves']
        self.basesAllowed = pitcherData['basesAllowed']
