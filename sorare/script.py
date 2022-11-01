import pandas as pd
from itertools import combinations

data = pd.read_excel('sorare_common.xlsx')
# data = pd.read_excel('anton.xlsx')
# data = pd.read_excel('sorare_limited.xlsx')
data_values = []

for i in data.values:
    data_values.append({"name": i[0], "score": i[1], "projection_score": i[2]})


def sorare(data_values, print_logs=False):
    comb = combinations(data_values, 4)
    team_comb = list(comb)
    team_score = {}
    for index, value in enumerate(team_comb):
        sum_team = sum([x["score"] for x in value])
        projection_team = sum([x["projection_score"] for x in value])
        if sum_team > 120:
            continue
        team_score.update({index: projection_team})

    team_score = dict(reversed(sorted(team_score.items(), key=lambda item: item[1])))

    team_count = 0
    projection_score_max = 0
    team_index = 0
    team_index_count = 0
    sum_team_scoring = 0
    for key, score_value in team_score.items():
        teams = team_comb[key]
        projection_score_sum = 0
        team_count += 1
        if print_logs:
            print(f"\t\tTeam count {team_count}")
        for team in teams:
            projection_score_sum += team["projection_score"]
            if print_logs:
                print(team["name"], team["score"])
        if print_logs:
            # print(f"Sum SCORE Team {score_value}")
            print(f"Projection Score SUM {projection_score_sum}")
        if projection_score_sum > projection_score_max:
            projection_score_max = projection_score_sum
            team_index = team_count
            team_index_count = key
            sum_team_scoring = score_value
        if print_logs:
            print("=" * 40)

    for team in team_comb[team_index_count]:
        print(team)
    print(f"Team Number {team_index}\n"
          f"Projection Score {projection_score_max},\n"
          f"Team Score {sum_team_scoring}\n")


sorare(data_values, print_logs=False)


