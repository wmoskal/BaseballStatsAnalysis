from Player import Player

class Pitcher(Player):

    def __init__(self, **pitcherData):
        stats_included = self.getIncludedStats(**pitcherData)
        self.stats_missing = self.getMissingStats(**pitcherData)
        for stat in stats_included:
            setattr(self, stat, pitcherData[stat])
        for stat in self.stats_missing:
            setattr(self, stat, None)
        
    def getMissingStats(self, **pitcherData):
        all_stats = [
            "age", "firstName", "lastName", "team_full",
            "team_abbrev", "position", "player_id",
            "gidp", "h9", "sac", "np", "gf", "bqs", "sho",
            "gidp_opp", "bk", "kbb", "hr9", "sv", "whip",
            "tbf", "bb9", "wp", "sf", "hb", "cs", "cg", "gs",
            "ibb", "pk", "irs", "wpct", "era", "rs9", "qs", "ir",
            "hld", "k9", "l", "svo", "ip", "w", 
            "s", "spct", "pip", "go", "ao", "g",
            "ab", "h", "db", "tr", "hr", "bb",
            "r", "so", "sb", "go_ao", "ppa",
            "babip", "avg", "slg", "obp", "ops", "year" ]
        stats_missing = pitcherData.keys()
        return list(set(all_stats) - set(stats_missing))

    def getIncludedStats(self, **pitcherData):
        all_stats = [
            "age", "firstName", "lastName", "team_full",
            "team_abbrev", "position", "player_id",
            "gidp", "h9", "sac", "np", "gf", "bqs", "sho",
            "gidp_opp", "bk", "kbb", "hr9", "sv", "whip",
            "tbf", "bb9", "wp", "sf", "hb", "cs", "cg", "gs",
            "ibb", "pk", "irs", "wpct", "era", "rs9", "qs", "ir",
            "hld", "k9", "l", "svo", "ip", "w", 
            "s", "spct", "pip", "go", "ao", "g",
            "ab", "h", "db", "tr", "hr", "bb",
            "r", "so", "sb", "go_ao", "ppa",
            "babip", "avg", "slg", "obp", "ops", "year" ]
        stats_included = pitcherData.keys()
        return list(set(all_stats).intersection(stats_included))

    def __str__(self):
        return(self.firstName + " " + self.lastName + " " + str(self.age) + " " + self.player_id + " " + self.year)
