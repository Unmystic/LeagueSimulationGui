import csv
import random


class Match:

    def __init__(self, homeTeam, awayTeam, table):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.table = table

        self.game = self.result(self.homeTeam, self.awayTeam )

    def match_data(self):
        return self.game, self.table

    def result(self, x, y):
        """Determine result of the game based on goals scored"""
        sc1 = self.goals(1.05 * float(x["rating"]))
        sc2 = self.goals(0.95 * float(y["rating"]))

        if sc1 > sc2:
            for team in self.table:
                if x['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc1
                    team['goalsConceded'] = team['goalsConceded'] + sc2
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['wins'] += 1
                    team['points'] = team['points'] + 3

                elif y['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc2
                    team['goalsConceded'] = team['goalsConceded'] + sc1
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['losses'] += 1

            return f"Team {x['name']} beat Team {y['name']} with score {sc1}:{sc2}"

        elif sc2 > sc1:
            for team in self.table:
                if y['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc2
                    team['goalsConceded'] = team['goalsConceded'] + sc1
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['wins'] += 1
                    team['points'] = team['points'] + 3

                elif x['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc1
                    team['goalsConceded'] = team['goalsConceded'] + sc2
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['losses'] += 1

            return f"Team {x['name']} lost to Team {y['name']} with score {sc1}:{sc2}"

        elif sc1 == sc2:
            for team in self.table:
                if x['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc1
                    team['goalsConceded'] = team['goalsConceded'] + sc2
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['draws'] += 1
                    team['points'] = team['points'] + 1

                elif y['name'] in team.values():
                    team['gamesPlayed'] = team['gamesPlayed'] + 1
                    team['goalsScored'] = team['goalsScored'] + sc2
                    team['goalsConceded'] = team['goalsConceded'] + sc1
                    goalDifference = team['goalsScored'] - team['goalsConceded']
                    if goalDifference > 0:
                        team['goalDifference'] = f"+{goalDifference}"
                    else:
                        team['goalDifference'] = f"{goalDifference}"
                    team['draws'] += 1
                    team['points'] = team['points'] + 1

            return f"Team {x['name']} draw Team {y['name']} with score {sc1}:{sc2}"

    def goals(self, r):
        """Determine goals scored by  the team based on rating"""
        # print(r)
        rating = r
        goal = [0, 1]
        weights = [50, 50]
        if rating < 70:
            weights = [60, 40]
        elif 70 < rating < 75:
            weights = [50, 50]
        elif 75 < rating < 80:
            weights = [45, 55]
        elif 80 < rating < 85:
            weights = [40, 60]
        elif 85 < rating < 90:
            weights = [35, 65]
        elif 90 < rating < 95:
            weights = [25, 75]
        elif rating > 95:
            weights = [10, 90]

        # weights = [100 - rating , rating]
        # print(weights)

        final = round(sum(random.choices(goal, weights, k=5)))

        return final