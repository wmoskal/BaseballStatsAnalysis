import datetime
from Batter import Batter
from Pitcher import Pitcher
from math import floor

class Parser:
    
    # Get the API URLs for rosters, batter stats, and pitcher stats and replace the parameters with their actual values 
    def getRosterLookupString(self, db, season_start, season_end, teamName):
        '''Get the roster lookup string and populate the parameters with values'''
        getRosterUrl = db.getRosterLookupURL()
        gru = getRosterUrl.replace('{start_season}', season_start)
        gru = gru.replace('{end_season}', season_end)
        gru = gru.replace('{team_id}', db.getRosterID(teamName))
        return gru
    
    # Get API hitting stats url and replace the parameters with their actual values
    def getHittingStatsLookup(self, db, season, playerId):
        '''Get the hitting stats lookup and populate the parameters with values'''
        getHittingUrl = db.getHittingLookupURL()
        ghu = getHittingUrl.replace('{season}', season)
        ghu = ghu.replace('{player_id}', playerId)
        return ghu

    # Get API pitching stats url and replace the parameters with their actual values
    def getPitchingStatsLookup(self, db, season, playerId):
        '''Get the pitching stats lookup url and populate the parameters with values'''
        getPitchingUrl = db.getPitchingLookupURL()
        gpu = getPitchingUrl.replace('{season}', season)
        gpu = gpu.replace('{player_id}', playerId)
        return gpu

    # Parse Batter and Pitcher info
    def parseBatter(self, db, http, player, year):
        '''parse batter info'''
        player_info = self.parsePlayerInfo(player, year)
        stat_url = self.getHittingStatsLookup(db, year, player_info['player_id'])
        batterStats = http.getBatterStatsFromURL(stat_url)
        return self.createBatter(player_info, batterStats)

    # parse a pitcher and return a Pitcher object
    def parsePitcher(self, db, http, player, year):
        '''parse pitcher info'''
        player_info = self.parsePlayerInfo(player, year)
        stat_url = self.getPitchingStatsLookup(db, year, player_info['player_id'])
        pitcherStats = http.getPitcherStatsFromURL(stat_url)
        return self.createPitcher(player_info, pitcherStats)
        
    # parse the player info    
    def parsePlayerInfo(self, player, year):
        player_info = {}
        player_info['age'] = self.getAge(player['birth_date'])
        first, last = player['name_first_last'].rsplit(" ", 1)
        player_info['firstName'] = first
        player_info['lastName'] = last
        #player_info['team_name'] = player['team_name']
        #player_info['team_abrieviation'] = player['team_abbrev']
        player_info['player_id'] = player['player_id']
        player_info['position'] = player['primary_position']
        player_info['year'] = str(year)
        return player_info

    # creates a batter object initialized with the stats
    def createBatter(self, player_info, batter_stats):
        try:
            batter_stats.update(player_info)
        except AttributeError:
            return None
        batter = Batter(**batter_stats)
        return batter

    # creates a pitcher object initialized with the stats
    def createPitcher(self, player_info, pitcher_stats):
        try:
            pitcher_stats.update(player_info)
        except AttributeError:
            return None
        pitcher = Pitcher(**pitcher_stats)
        return pitcher

    # get a player from a roster by the index of the player
    def getPlayerByIndex(self, roster, i):
        return roster[i]

    # get a player from a roster by the name of the player
    def getPlayerByName(self, roster, firstName, lastName):
        player = None
        i = 0
        fullName = firstName + " " + lastName
        for r in roster:
            if r['name_display_first_last'] == fullName:
                player = roster[i]
            i += 1
        return player

    # get a player from a roster by the players id
    def getPlayerById(self, roster, pid):
        player = None
        i = 0
        for r in roster:
            if r['player_id'] == pid:
                player = roster[i]
            i += 1
        return player 
            
    # get the value of a player
    def getPlayerValue(self, player, key):
        return player[key]        

    # convert a players birth date into their age in years
    def getAge(self, dob):
        dob = datetime.datetime.strptime(dob.split('T')[0], "%Y-%m-%d").date()
        today = datetime.date.today()
        age = today - dob
        age = age.days / 365
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        return floor(age)
