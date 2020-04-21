import requests

class HTTPData:

    def getRosterFromURL(self, urlString):
        request = requests.get(urlString)
        requestData = request.json()
        rosterTeam = requestData['roster_team_alltime']
        queryResults = rosterTeam['queryResults']
        try:
            row = queryResults['row']
        except KeyError:
            return None
        return row

    def getBatterStatsFromURL(self, url):
        request = requests.get(url)
        requestData = request.json()
        hitting = requestData['sport_hitting_tm']
        queryResults = hitting['queryResults']
        try:
            row = queryResults['row']
        except KeyError:
            return None
        return row

    def getPitcherStatsFromURL(self, url):
        request = requests.get(url)
        requestData = request.json()
        pitching = requestData['sport_pitching_tm']
        queryResults = pitching['queryResults']
        try:
            row = queryResults['row']
        except KeyError:
            return None
        return row