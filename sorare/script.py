import pandas as pd
from itertools import combinations

print(" 1: julia.xlsx\n 2: sorare_common.xlsx\n 3: anton.xlsx\n 4: sorare_limited.xlsx")
what_file = int(input("What file do you whant to read?\n"))
data_values = []
cards = int(input("How many cards do you need (4 or 5)?\n"))


def get_file_to_read():
    global data
    if what_file == 1:
        data = pd.read_excel('julia.xlsx')
    elif what_file == 2:
        data = pd.read_excel('sorare_common.xlsx')
    elif what_file == 3:
        data = pd.read_excel('anton.xlsx')
    elif what_file == 4:
        data = pd.read_excel('sorare_limited.xlsx')
    else:
        print("Please check what option did you choose... P.S. must something like 1 or 2 or 3 or 4")
    return data


def get_conditions():
    global remaining_points
    if cards == 4:
        remaining_points = 120
    elif cards == 5:
        remaining_points = 110
    else:
        get_conditions()
    return remaining_points


def getting_all_data_and_values():
    get_file_to_read()
    for i in data.values:
        data_values.append({"name": i[0], "score": i[1], "projection_score": i[2]})


def sorare(data_values, print_logs=False):
    get_file_to_read()
    get_conditions()
    getting_all_data_and_values()
    comb = combinations(data_values, cards)
    team_comb = list(comb)
    team_score = {}
    for index, value in enumerate(team_comb):
        sum_team = sum([x["score"] for x in value])
        projection_team = sum([x["projection_score"] for x in value])
        if sum_team > remaining_points:
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


