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

    show_pack_cards = int(input("How many teams do you wanna print?\n"))
    show_team = 0
    for key, score_value in team_score.items():
        teams = team_comb[key]
        show_team += 1

        if show_team <= show_pack_cards:
            total_team_score = 0
            total_team_projection_score = 0
            for team in teams:
                total_team_score += team["score"]
                total_team_projection_score += team["projection_score"]
                print(team)
            print(f"Team Score {total_team_score} Projection Score {total_team_projection_score}")
            print("=" * 70)
        else:
            break


sorare(data_values)


