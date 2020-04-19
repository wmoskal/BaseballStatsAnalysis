import psycopg2

class DB:

    cursor = None
    connection = None

    def __init__(self):    
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                password = "Moskalromak1",
                                host = "localhost",
                                port = "5433",
                                database = "postgres")

            self.cursor = self.connection.cursor()
            print (self.connection.get_dsn_parameters(),"\n")

            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record,"\n")
        except (Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)

    def execute(self, sql):
        self.cursor.execute(sql)

    def close(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

    def insert(self, table, columns, data):
        self.cursor.execute("INSERT INTO " + table + " " + self.formatInsertString(columns) + " VALUES" + self.formatInsertString(data))

    def insertRow(self, table, data):
        self.cursor.execute("INSERT INTO " + table + " " + " VALUES" + self.formatInsertString(data)) 

    def formatInsertString(self, items):
        '''Format insert strings, either columns or values (lists) into strings'''
        if len(items) == 1:
            return "(" + items[0] + ")"
        strFormat = "("
        for i in items:
            strFormat += i + ","
        strFormat = strFormat[:-1]
        strFormat += ")"
        return strFormat

    def getRosterID(self, teamName):
        self.cursor.execute("SELECT team_id FROM roster_id_lookup WHERE team_name='" + teamName + "'")
        rosterID = self.cursor.fetchone()
        return rosterID[0]

    def getRosterLookupURL(self):
        self.cursor.execute("SELECT url FROM lookup_urls WHERE id=1")
        lookupUrl = self.cursor.fetchone()[0]
        return lookupUrl

    
    ###### init methods ######
    def insertLookupUrls(self):
        '''Writes the 3 relevant lookup urls (hardcoded for now) into the lookup_urls table'''
        self.cursor.execute("""INSERT INTO lookup_urls (id, url, description)
            VALUES(1, 'http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season=''{start_season}''&end_season=''{end_season}''&team_id=''{team_id}''', 'Retrieves a roster for a team and a year'),
            (2, 'http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id=''mlb''&game_type=''R''&season=''{season}''&player_id=''{player_id}''', 'gets the hitting stats for a player for a year'),
            (3, 'http://lookup-service-prod.mlb.com/json/named.sport_pitching_tm.bam?league_list_id=''mlb''&game_type=''R''&season=''{season}''&player_id=''{player_id}''', 'gets the pitching stats for a player for a year')
            """)
        self.connection.commit()

    def rosterIdsToDB(self):
        '''writes each team/ roster id to the table roster_id_lookup. Hardcoded strings for now'''
        self.cursor.execute("""INSERT INTO roster_id_lookup (team_name, team_id)
            VALUES('Los Angeles Angels', '108'),
            ('Arizona Diamondbacks', '109'),
            ('Baltimore Orioles', '110'),
            ('Boston Red Sox', '111'),
            ('Chicago Cubs', '112'),
            ('Cincinnati Reds', '113'),
            ('Cleveland Indians', '114'),
            ('Colorado Rockies', '115'),
            ('Detroit Tigers', '116'),
            ('Houston Astros', '117'),
            ('Kansas City Royals', '118'),
            ('Los Angeles Dodgers', '119'),
            ('Washington Nationals', '120'),
            ('New York Mets', '121'),
            ('Oakland Athletics', '133'),
            ('Pittsburgh Pirates', '134'),
            ('San Diego Padres', '135'),
            ('Seattle Mariners', '136'),
            ('San Francisco Giants', '137'),
            ('St. Louis Cardinals', '138'),
            ('Tampa Bay Rays', '139'),
            ('Texas Rangers', '140'),
            ('Toronto Blue Jays', '141'),
            ('Minnesota Twins', '142'),
            ('Philadelphia Phillies', '143'),
            ('Atlanta Braves', '144'),
            ('Chicago White Sox', '145'),
            ('Miami Marlins', '146'),
            ('New York Yankees', '147'),
            ('Milwaukee Brewers', '158')
           """)
        self.connection.commit()
