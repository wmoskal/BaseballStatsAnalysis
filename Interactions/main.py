import requests
from HTTPData import HTTPData
from Parser import Parser
from DB import DB

def main():
    # test the interaction classes here
    # roster link: "http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2017'"

    # base class objects used for 
    http = HTTPData()
    parser = Parser()
    db = DB()
    rs = parser.getRosterLookupString(db, '2017', '2018', 'Toronto Blue Jays')
    blueJaysRoster = http.getRosterFromURL(rs)
    print(len(blueJaysRoster))

if __name__ == "__main__":
    main()