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
        moments = random.choice([3, 4, 5, 6, 7])
        sc1 = self.goals(attack=(1.05 * x["rating"]['attackRating'] * (x["rating"]['teamCohesion'] / 100)),
                         defence=y["rating"]['defenceRating'], moments=moments)
        sc2 = self.goals(attack=(y["rating"]['attackRating'] * (y["rating"]['teamCohesion'] / 100)),
                         defence=x["rating"]['defenceRating'], moments=moments)

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

    def goals(self, attack, defence, moments):
        """Determine goals scored by  the team based on rating"""
        # print(r)
        goal = [0, 1]
        scoring_chance = 50 + (attack - defence)
        weights = [100 - scoring_chance,scoring_chance]
        final = round(sum(random.choices(goal, weights, k=moments)))

        return final