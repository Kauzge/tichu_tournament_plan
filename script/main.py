"""Main script for the creation of a Tichu tournament plan"""

from random import shuffle
from input import get_input
from output import print_tournament_plan
from excel import create_excel

def get_shuffled_players(players:list) -> list:
    """Create a shuffled copy of the players list"""
    players_copy = players.copy()
    shuffle(players_copy)
    return players_copy

def check_duplicate(current_match:list, current_table:list, player:int) -> bool:
    """
    Checks if the player is already sitting at the current table
    or at another table in the current match
    """
    if player in current_table:
        # Player is already sitting at the current table
        return True
    if current_match != []:
        for table in current_match:
            if player in table:
                # Player is already sitting at another table in the current match
                return True
    # Player is not sitting at the current table
    # and not sitting at another table in the current match
    return False

def select_fitting_player(remaining_players:list, current_match:list, current_table:list) -> int:
    """
    Selects a player from the list of remaining players that is not sitting
    at the current table or at another table in the current match
    """
    while True:
        selected_player = remaining_players.pop(0)
        if check_duplicate(current_match, current_table, selected_player):
            # Return selected player to the list of remaining players if he is not fitting
            remaining_players.append(selected_player)
        else:
            return selected_player

def check_combinations(tournament_plan:list) -> bool:
    """Checks if the same combination of players is on multiple tables in the tournament"""
    found_combinations = []
    for match in tournament_plan:
        for table in match:
            for i in range(0, len(table), 2):
                # Loop through the match list in steps of 2 and get the teams of each match
                team = table[i:i+2]
                if team in found_combinations or team[::-1] in found_combinations:
                    # If the team is already in the found_combinations list, return True
                    return True
                found_combinations.append(team)
    # If no combination is found twice, return False
    return False

def generate_tournament_plan(players:list, number_of_matches:int, number_of_tables:int) -> list:
    """Build the tournament_plan list based on the number of matches and tables"""
    tournament_plan = []

    remaining_players = get_shuffled_players(players)
    for _ in range(number_of_matches):
        current_match = []
        for _ in range(number_of_tables):
            current_table = []
            for _ in range(4):
                # Every match has 4 players per table
                if not remaining_players:
                    # Reshuffle the players if the list of remaining players is empty
                    remaining_players = get_shuffled_players(players)
                current_table.append(select_fitting_player(remaining_players,
                                                           current_match, current_table))
            current_match.append(current_table)
        tournament_plan.append(current_match)
    return tournament_plan

if __name__ == "__main__":
    num_players, num_matches, use_terminal = get_input()
    num_tables = num_players // 4
    player_list = list(range (1, num_players+1))
    if num_matches < num_players:
        # This surely can be optimized, but it works for now
        while True:
            tp = generate_tournament_plan(player_list, num_matches, num_tables)
            if not check_combinations(tp):
                break
    else:
        # If the number of matches is equal or higher than the number of players,
        # the tournament plan is generated without checking for combinations
        tp = generate_tournament_plan(player_list, num_matches, num_tables)
    if use_terminal:
        print_tournament_plan(tp, num_tables)
    else:
        create_excel(player_list, tp, num_players, num_tables, num_matches)
