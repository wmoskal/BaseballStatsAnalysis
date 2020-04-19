import datetime

class Parser:

    def getRosterLookupString(self, db, season_start, season_end, teamName):
        getRosterUrl = db.getRosterLookupURL()
        gru = getRosterUrl.replace('{start_season}', season_start)
        gru = gru.replace('{end_season}', season_end)
        gru = gru.replace('{team_id}', db.getRosterID(teamName))
        return gru

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
    
    def parseBatterInfo(self, personal, stats):
        batterInfo = {}
        batterInfo['age'] = getAge(personal['birth_date'])
        batterInfo['first_name'] = personal['name_first']
        batterInfo['last_name'] = personal['name_last']
        batterInfo['team_name'] = personal['team_name']
        batterInfo['team_abrieviation'] = personal['team_abbrev']
        batterInfo['player_id'] = personal['player_id']
        batterInfo['positions'] = personal['position_txt']
        

    def getAge(self, dob):
        today = datetime.date.today()
        age = dob - today
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        return age