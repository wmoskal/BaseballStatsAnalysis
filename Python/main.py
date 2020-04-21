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
    url = parser.getRosterLookupString(db, '2018', '2019', 'Toronto Blue Jays')
    roster = http.getRosterFromURL(url)
    for r in roster:
        if r['primary_position'] != 'P':
            parser.parseBatter(db, http, r, '2018')
        else:
            parser.parsePitcher(db, http, r, '2018')


if __name__ == "__main__":
    #sys.path.append('D:\\Documents\\Side Projects\\BaseballAnalysis\\baseball-analysis\\Interactions')
    main()