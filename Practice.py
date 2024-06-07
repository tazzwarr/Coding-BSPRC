import random


def choose():
    min_value = 1
    max_value = 5
    choose = random.randint(min_value, max_value)

    return choose


while True:
    players = input("Enter the number of players (2 - 5): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Must be between 2 - 5 players.")
    else:
        print("Invalid, try again.")

max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_choose = input("Would you like to choose (y)? ")
            if should_choose.lower() != "y":
                break

            value = choose()
            if value == 1:
                print("You chose a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You chose a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
