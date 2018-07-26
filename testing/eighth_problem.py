def rock_paper_scissors():
    player_1_input = input("Player 1, please enter either rock, paper or scissors:")
    player_2_input = input("Player 2, please enter either rock, paper or scissors:")
    adjusted_player_1 = player_1_input.lower()
    adjusted_player_2 = player_2_input.lower()
    while adjusted_player_1 == adjusted_player_2:
        player_1_input = input("That's a draw. Player 1, please enter either rock, paper or scissors:")
        player_2_input = input("Player 2, please enter either rock, paper or scissors:")
        adjusted_player_1 = player_1_input.lower()
        adjusted_player_2 = player_2_input.lower()
        continue
    else:
        if adjusted_player_1 == "rock" and adjusted_player_2 == "paper" or adjusted_player_1 == "paper" and adjusted_player_2 == "scissors" or adjusted_player_1 == "scissors" and adjusted_player_2 == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
rock_paper_scissors()
