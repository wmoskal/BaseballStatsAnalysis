import datetime
from Batter import Batter
from Pitcher import Pitcher

class Parser:

    # Get the API URLs for rosters, batter stats, and pitcher stats and replace the parameters with their actual values 
    def getRosterLookupString(self, db, season_start, season_end, teamName):
        '''Get the roster lookup string and populate the parameters with values'''
        getRosterUrl = db.getRosterLookupURL()
        gru = getRosterUrl.replace('{start_season}', season_start)
        gru = gru.replace('{end_season}', season_end)
        gru = gru.replace('{team_id}', db.getRosterID(teamName))
        return gru
    
    def getHittingStatsLookup(self, db, season, playerId):
        '''Get the hitting stats lookup and populate the parameters with values'''
        getHittingUrl = db.getHittingLookupURL()
        ghu = getHittingUrl.replace('{season}', season)
        ghu = ghu.replace('{player_id}', playerId)
        return ghu

    def getPitchingStatsLookup(self, db, season, playerId):
        '''Get the pitching stats lookup url and populate the parameters with values'''
        getPitchingUrl = db.getPitchingLookupURL()
        gpu = getPitchingUrl.replace('{season}', season)
        gpu = gpu.replace('{player_id}', playerId)
        return gpu

    # Parse Batter and Pitcher info
    def parseBatter(self, db, http, player, year):
        '''parse batter info'''
        player_info = self.parsePlayerInfo(player)
        stat_url = self.getHittingStatsLookup(db, year, player_info['player_id'])
        batterStats = http.getBatterStatsFromURL(stat_url)
        self.createBatter(player_info, batterStats)

    def parsePitcher(self, db, http, player, year):
        '''parse pitcher info'''
        player_info = self.parsePlayerInfo(player)
        stat_url = self.getPitchingStatsLookup(db, year, player_info['player_id'])
        pitcherStats = http.getPitcherStatsFromURL(stat_url)
        self.createPitcher(player_info, pitcherStats)
        
    def parsePlayerInfo(self, player):
        player_info = {}
        # player_info['age'] = getAge()
        first, last = player['name_first_last'].rsplit(" ", 1)
        player_info['first_name'] = first
        player_info['last_name'] = last
        #player_info['team_name'] = player['team_name']
        #player_info['team_abrieviation'] = player['team_abbrev']
        player_info['player_id'] = player['player_id']
        player_info['position'] = player['primary_position']
        return player_info


    def createBatter(self, player_info, batter_stats):
        print("player info: " + str(player_info))
        print('\n')
        print("batter stats: " + str(batter_stats))
        print('\n')

    def createPitcher(self, player_info, pitcher_info):
        print("player info " + str(player_info))
        print('\n')
        print("pitcher stats" + str(pitcher_info))
        print("\n")

    def getPlayerByIndex(self, roster, i):
        return roster[i]

    def getPlayerByName(self, roster, firstName, lastName):
        player = None
        i = 0
        fullName = firstName + " " + lastName
        for r in roster:
            if r['name_display_first_last'] == fullName:
                player = roster[i]
            i += 1
        return player

    def getPlayerById(self, roster, pid):
        player = None
        i = 0
        for r in roster:
            if r['player_id'] == pid:
                player = roster[i]
            i += 1
        return player 
            
    def getPlayerValue(self, player, key):
        return player[key]        

    def getAge(self, dob):
        today = datetime.date.today()
        age = dob - today
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        return age