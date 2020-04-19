import requests

class HTTPData:

    def getRosterFromURL(self, urlString):
        request = requests.get(urlString)
        requestData = request.json()
        rosterTeam = requestData['roster_team_alltime']
        queryResults = rosterTeam['queryResults']
        row = queryResults['row']
        return row

    def getBatterStatsFromURL(self, player_id, season):
        request = requests.get("http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='" + season +"'&player_id='" + player_id + "'")
        requestData = request.json()
        hitting = requestData['sport_hitting_tm']
        queryResults = hitting['queryResults']
        row = queryResults['row']
        print(row)