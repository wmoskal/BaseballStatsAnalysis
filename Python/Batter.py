from Player import Player
import numbers

class Batter(Player):

    def __init__(self, **batterData):
        stats_included = self.getIncludedStats(**batterData)
        self.stats_missing = self.getMissingStats(**batterData)
        for stat in stats_included:
            setattr(self, stat, batterData[stat])
        for stat in self.stats_missing:
            setattr(self, stat, None)

    def getMissingStats(self, **batterData):
        all_stats = [
            "age", "firstName", "lastName", "team_full",
            "team_abbrev", "player_id", "position",
            "g", "ab", "h", "r", "rbi", "hr", "bb", "so",
            "sb", "avg", "slg", "obp", "ops", "year", 
            "gidp", "sac", "np", "tb", "gidp_opp", "hbp",
            "wo", "sf", "cs", "go_ao", "ppa", "ibb", "roe",
            "go", "babip", "lob", "xbh", "d", "tpa", "t", "ao"]
        stats_missing = batterData.keys()
        return list(set(all_stats) - set(stats_missing))

    def getIncludedStats(self, **batterData):
        all_stats = [
            "age", "firstName", "lastName", "team_full",
            "team_abbrev", "player_id", "position",
            "g", "ab", "h", "r", "rbi", "hr", "bb", "so",
            "sb", "avg", "slg", "obp", "ops", "year", 
            "gidp", "sac", "np", "tb", "gidp_opp", "hbp",
            "wo", "sf", "cs", "go_ao", "ppa", "ibb", "roe",
            "go", "babip", "lob", "xbh", "d", "tpa", "t", "ao"]
        stats_included = batterData.keys()
        return list(set(all_stats).intersection(stats_included))

    def __str__(self):
        return(self.firstName + " " + self.lastName + " " + str(self.age) + " " + self.player_id + " " + self.year)

    def toDBString(self):
        dbString = "("
        attrs = ["age", "firstName", "lastName", "team_full",
            "team_abbrev", "player_id", "position",
            "g", "ab", "h", "r", "rbi", "hr", "bb", "so",
            "sb", "avg", "slg", "obp", "ops", "year", 
            "gidp", "sac", "np", "tb", "gidp_opp", "hbp",
            "wo", "sf", "cs", "go_ao", "ppa", "ibb", "roe",
            "go", "babip", "lob", "xbh", "d", "tpa", "t", "ao"]
        strings = ["firstName", "lastName", "team_full",
            "team_abbrev", "player_id", "position", "year"]
        for stat in attrs:
            attr = getattr(self, stat)
            if stat in strings:
                if "'" in attr:
                    attr = attr.replace("'", "''")
                    print(attr)
                dbString += "'" + attr + "',"
            else:
                if not isinstance(attr, numbers.Number):
                    dbString += "NULL,"
                    continue
            
                dbString += str(attr) + ","
        dbString = dbString[:-1] + ')'
        return dbString