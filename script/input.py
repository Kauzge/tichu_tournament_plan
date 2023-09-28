import argparse

def get_input():
    # Get the number of players and rounds from the command line
    parser = argparse.ArgumentParser(description="This script to creates a Tichu tournament plan with a given number of players and rounds")
    parser.add_argument('-p', '--players', type=int, default=8, help='Number of Players')
    parser.add_argument('-r', '--rounds', type=int, default=6, help='Number of Rounds')
    parser.add_argument('-t', '--terminal', action='store_true', default=False, help='Set this flag to print the tournament plan to the terminal')

    args = parser.parse_args()
    number_of_players = args.players
    number_of_rounds = args.rounds
    use_terminal = args.terminal

    if number_of_players < 4:
        raise ValueError("The number of players must be at least 4")
    elif number_of_rounds < 1:
        raise ValueError("The number of rounds must be at least 1")
    else:
        return number_of_players, number_of_rounds, use_terminal

