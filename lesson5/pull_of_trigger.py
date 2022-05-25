score = 100
loop_action = 1

while loop_action <= 4:
    action = input("Choose one of 'hit' or 'miss': ")
    if action in ("hit", "miss"):
        if action == "miss":
            score -= 20
        elif action == "hit":
            score += 10
        loop_action += 1
    else:
        print("Is not correct action")

print(score)
