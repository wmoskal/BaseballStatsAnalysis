import requests
from HTTPData import HTTPData
from Parser import Parser
from DB import DB
from Batter import Batter
from Pitcher import Pitcher

def main():
    # test the interaction classes here
    # roster link: "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2017'"

    # base class objects used for 
    
    http = HTTPData()
    parser = Parser()
    db = DB()
    teams = db.getRosterIDs()
    batters = []
    for team in teams:
        url = parser.getRosterLookupString(db, '2018', '2019', team[0])
        roster = http.getRosterFromURL(url)
        for r in roster:
            if r['primary_position'] != 'P':
                batter = parser.parseBatter(db, http, r, '2018')
                if batter:
                    batters.append(batter)
            '''else:
                pitcher = parser.parsePitcher(db, http, r, '2018')
                if pitcher:
                    # print(pitcher)
                    print()'''
    try:
        err = db.insertBatters(batters)
        print('err' + str(err))
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()