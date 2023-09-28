from random import shuffle
from input import get_input
from output import print_tournament_plan
from excel import create_excel

def get_shuffled_players(players:list) -> list:
    players_copy = players.copy()
    shuffle(players_copy)
    return players_copy

def check_duplicate(current_round:list, current_table:list, player:int) -> bool:
    if player in current_table:
        # Player is already sitting at the current table
        return True
    elif current_round != []:
        for table in current_round:
            if player in table:
                # Player is already sitting at another table in the current round
                return True
    # Player is not sitting at the current table and not sitting at another table in the current round
    return False

def select_fitting_player(remaining_players:list, current_round:list, current_table:list) -> int:
    while True:
        selected_player = remaining_players.pop(0)
        if check_duplicate(current_round, current_table, selected_player):
            # Return selected player to the list of remaining players if he is not fitting
            remaining_players.append(selected_player)
        else:
            return selected_player

def check_combinations(tournament_plan:list) -> bool:
    # Checks if the same combination of players is on multiple tables in the tournament
    found_combinations = []
    for round in tournament_plan:
        for table in round:
            for i in range(0, len(table), 2):
                # Loop through the match list in steps of 2 and get the teams of each match
                team = table[i:i+2]
                if team in found_combinations or team[::-1] in found_combinations:
                    # If the team is already in the found_combinations list, return True
                    return True
                found_combinations.append(team)
    # If no combination is found twice, return False
    return False

def generate_tournament_plan(players:list, number_of_rounds:int, number_of_tables:int) -> list:
    # Build the tournament_plan list based on the number of rounds and tables
    tournament_plan = []

    remaining_players = get_shuffled_players(players)
    for round in range(number_of_rounds):
        current_round = []
        for table in range(number_of_tables):
            current_table = []
            for player in range(4):
                if remaining_players == []:
                    # Reshuffle the players if the list of remaining players is empty
                    remaining_players = get_shuffled_players(players)
                current_table.append(select_fitting_player(remaining_players, current_round, current_table))
            current_round.append(current_table)
        tournament_plan.append(current_round)
    return tournament_plan

if __name__ == "__main__":
    number_of_players, number_of_rounds, use_terminal = get_input()
    number_of_tables = number_of_players // 4
    players = [x for x in range (1, number_of_players+1)]
    if number_of_rounds < number_of_players:
        # This surely can be optimized, but it works for now
        while True:
            tournament_plan = generate_tournament_plan(players, number_of_rounds, number_of_tables)
            if not check_combinations(tournament_plan):
                break
    else:
        # If the number of rounds is equal or higher than the number of players, the tournament plan is generated without checking for combinations
        tournament_plan = generate_tournament_plan(players, number_of_rounds, number_of_tables)
    if use_terminal:
        print_tournament_plan(tournament_plan, number_of_tables)
    else:
        create_excel(players, tournament_plan, number_of_players, number_of_tables, number_of_rounds)

